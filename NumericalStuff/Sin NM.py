import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y,t):

    z1, z2 = y
    dydt = [z2, -z1]
    return dydt

y0 = [0, 1]
domain = 2*np.pi
t = np.linspace(0, domain, 101)

y = odeint(func, y0, t)

plt.plot(t,y[:, 0], 'b', label='y(t)')
plt.plot(t, y[:, 1], 'g', label="y'(t)")
plt.xlabel("Time")
plt.ylabel("Y")

exact_t = np.linspace(0, domain, 10)
exact_y = np.sin(exact_t)
plt.plot(exact_t, exact_y, 'o', color='r', label='exact')
plt.legend()
plt.show()

