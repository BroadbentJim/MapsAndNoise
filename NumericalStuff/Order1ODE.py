import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.stats import norm

def func(y,t):


    dydt = (1/np.sqrt(np.pi))*np.exp(-t**2)
    return dydt

y0 = 0.5
domain = 5
t = np.linspace(0, domain, 101)

y = odeint(func, y0, t)

plt.plot(t,y, 'b', label='y(t)')
plt.xlabel("Time")
plt.ylabel("Y")

exact_t = np.linspace(0, domain, 10)
exact_y = norm.cdf(exact_t)
plt.plot(exact_t, exact_y, 'o', color='r', label='exact')
plt.legend()
plt.show()

