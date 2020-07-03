import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Analysis():
    """
    My personal class for fast analysis
    """
    
    def __init__(self, arg = 15):
        self.class_var = 13
        if arg > 15:
            self.new_var=arg
        else:
            self.new_var=10
            
    def fast_single_plot(self, x, y, title=False):
        fig, ax = plt.subplots(1,1, tight_layout=True)
        
        ax.plot(x,y, "b-")
        if title:
            ax.set_title(title)
        fig.show()
        
    def GaussianFit(self, data, bin_nr=False, printinfo=False, showmu=False, showsigma=False, savefig=False):
        """
        Fct to create one Gaussian fit
        Args:
            data: numpy 1darray or list
        """
        from scipy.optimize import curve_fit
        # functions
        def gaussian(x, mu, sigma):
            """
            Gaussian distribution
            Args:
                - x values
                - mu
                - sigma
            Returns:
                gaussian curve
            """
            return (1/(sigma*np.sqrt(2*np.pi))*np.exp(- ((x - mu)**2)/(2*sigma**2)))
        
        if not bin_nr:
            binnr = int(np.sqrt(data.size))
        elif type(bin_nr)!=int:
            print("Attention: binnumber is not an int, using 30 as default value!")
            binnr = 30
        else:
            binnr = bin_nr
        
        vals, binedge = np.histogram(data, bins=binnr, density=True)
        
        # to overcome wrong positioning of the bins, compute the width of one bin and subtract half of it it to the edges
        bin_width = binedge[1] - binedge[0]
        bincenter = binedge[1:]- bin_width/2
        
        # compute the fit and little information
        opt_vals, cov_coeff = curve_fit(gaussian, bincenter, vals)
        
        if printinfo:
            print("optimal expected value mu: {}\noptimal standar deviation sigma: {}".format(*opt_vals))
        
        # =====================================================
        
        # plot everything
        mu, sigma = opt_vals[0], opt_vals[1]
        gauss_fit = gaussian(bincenter, *opt_vals)
        max_gauss = max(gauss_fit)
        
        # define the plot
        fig, ax = plt.subplots(1,1, figsize=(9,6), tight_layout=True)
        
        ax.hist(data, bins=binnr, density=True, label="distribution")
        ax.plot(bincenter, vals, "ro")
        
        label_text="$\mu$={:.3}, $\sigma^2$={:.3}".format(*opt_vals)
        ax.plot(bincenter, gauss_fit, 'r-', label=label_text)
        
        ax.set_xlabel("data")
        ax.legend()
        
        # find value for half max gauss
        half_max_idx = np.abs(gauss_fit - max_gauss/2).argmin()

        starting_bin = bincenter[half_max_idx]
        if starting_bin < mu:
            xmin, xmax = starting_bin, starting_bin + 2*sigma
        else:
            xmax, xmin = starting_bin, starting_bin - 2*sigma
        
        # # plot mu and sigma
        if showmu:
            ax.vlines(x=mu, color="grey", linestyle="--", ymin=0, ymax=max_gauss)
        if showsigma:
            ax.hlines(y=max_gauss/2, xmin=xmin, xmax=xmax, color="grey", linestyle="--")
            
        if savefig:
            fig.savefig("gaussian_fit_{}.pdf".format(savefig))
        else:
            fig.show()
            
    def ExponentianFit(self, data, args):
        """
        Fct for plotting an exponential fit to data
        """
        