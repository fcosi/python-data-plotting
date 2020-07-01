import matplotlib.pyplot as plt

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