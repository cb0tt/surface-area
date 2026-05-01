# Surface Area of Revolution Calculator 
#### Math 202, Dr. DeWitt


A Python calculator for finding the surface area generated when a curve is rotated around an axis. 

Both python file and notebook files are provided.

Given a curve:

$$
y = f(x)
$$

on the interval:

$$
a \le x \le b
$$

the program calculates the surface area formed by rotating the curve around a selected axis.

## Core Formulas


### Rotation Around the x-axis

$$
S = 2\pi \int_a^b f(x)\sqrt{1+\left(f'(x)\right)^2}\,dx
$$

### Rotation Around the y-axis

$$
S = 2\pi \int_a^b x\sqrt{1+\left(f'(x)\right)^2}\,dx
$$

Built with 
- SymPy
- NumPy
- Matplotlib
