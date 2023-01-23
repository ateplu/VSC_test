import numpy as np

def basic_sigmoid(x):
    """
    Compute sigmoid of x.
    """
 
    s = 1/(1+np.exp(-x))
    
    return s

bb = np.array([1,2])
aa = basic_sigmoid(bb)
print(aa)

