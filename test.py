#%%
from math import e
from pylab import *
from numpy import arange

re_range = 7
im_range = 7

def f(x):
    return e ** (x * 1j)

def plot_line(scalar, offset):
    line = [f(x * scalar + offset) for x in arange(-re_range, re_range, 0.1)]
    line = [(f.real, f.imag) for f in line]
    line = [*zip(*line)]

    plot(*line)

for i in arange(-im_range, im_range + 1, 1):
    plot_line(1, i * 1j)
    plot_line(1j, i)

grid()
show()
# %%
