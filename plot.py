import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
def plot(a, b, f, x, axis):
    #x = sp.symbols("x")
    f = sp.sympify(f)
    b = float(b)
    a = float(a)
    #axis = sp.sympify(axis)
    fx_numeric = sp.lambdify(x, f, modules="numpy") #make a function that accepts x and returns f(x)
    x_vals = np.linspace(a, b)
    spin = np.linspace(0, (2 * np.pi)) #0 --> 2pi represents one full rotation around axis
    xgrid, thetas = np.meshgrid(x_vals, spin) #xgrid all x values, thetas all rotation angles in grid
    fxgrid = fx_numeric(xgrid) # f(x) values on the grid
    if axis.lower().strip() == 'x':
        xdim = xgrid
        ydim = fxgrid * np.cos(thetas)
        zdim = fxgrid * np.sin(thetas) #z always gets sin in #D, in 2d y * sin,sin is matched with vertical axis
    elif axis.lower().strip() == 'y':
        xdim = xgrid* np.cos(thetas)
        ydim = fxgrid
        zdim = xgrid * np.sin(thetas)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(xdim, ydim, zdim)


    



