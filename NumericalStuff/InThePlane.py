import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def function(state, t):

    x, y = state
    dxdt = np.exp(x)
    dydt = np.sin(y-x)
    return dxdt, dydt

state0 = [1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)
states = odeint(function, state0, t)

fig = plt.figure()
ax = fig.gca()
ax.plot(states[:, 0], states[:, 1])
plt.show()