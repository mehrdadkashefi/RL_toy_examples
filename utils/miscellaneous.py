import numpy as np

# Moving average function
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w