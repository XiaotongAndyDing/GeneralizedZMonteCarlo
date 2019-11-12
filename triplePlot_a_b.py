import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from numpy import exp

b = np.linspace(0.01, 0.99, 100)


def int_a(b):
    return integrate.quad(lambda x: b * (exp(-x) - exp(-(1 - b) * x)) / (1 - exp(-x)), 0, 1 / b)[0]


plt.plot(b, [int_a(i) for i in b])
plt.plot(b, [-i*i for i in b])

plt.xlabel('b')
plt.ylabel('a')
plt.legend(['a(b)', 'y=-x^2'])
plt.show()
