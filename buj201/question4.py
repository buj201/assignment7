'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def grid_constructor(gran):
    ##gran specifies the granularity of the grid (number of intervals).
    ##It accepts positive integer inputs.
    input_valid = False 
    while not input_valid:
        if not (type(gran) == int and gran > 2):
            gran = int(raw_input('Invalid input. Specify new positive interger gran: '))
        else:
            input_valid = True
            
    x = np.linspace(-2,1,gran)
    y = np.linspace(-1.5,1.5,gran)
    xx, yy = np.meshgrid(x,y)
    return xx,yy

def generate_mandelbrot_set(grid_gran, N_max=50, some_threshold=50):
    x,y = grid_constructor(grid_gran)
    c = x + 1j*y
    z = c
    for v in range(N_max):
        z = z**2 + c
    mask = (np.abs(z) < some_threshold)
    import matplotlib.pyplot as plt
    plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png', dpi=1500)

def make_fractal(): 
    generate_mandelbrot_set(5000)
    print 'done'