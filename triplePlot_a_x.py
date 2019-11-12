import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from numpy import exp

b = 0.5
x_05 = np.linspace(0.01, 1 / b, 500)
a_in_integral_05 = [b * (np.exp(-i) - np.exp(-(1 - b) * i)) / (1 - np.exp(-i)) for i in x_05]

b = 0.3
x_03 = np.linspace(0.01, 1 / b, 500)
a_in_integral_03 = [b * (np.exp(-i) - np.exp(-(1 - b) * i)) / (1 - np.exp(-i)) for i in x_03]

b = 0.7
x_07 = np.linspace(0.01, 1 / b, 500)
a_in_integral_07 = [b * (np.exp(-i) - np.exp(-(1 - b) * i)) / (1 - np.exp(-i)) for i in x_07]

plt.subplot(1, 2, 1)
plt.plot(x_03, a_in_integral_03, x_05, a_in_integral_05, x_07, a_in_integral_07)
plt.fill_between(x_03, a_in_integral_03, alpha=0.1)
plt.fill_between(x_05, a_in_integral_05, alpha=0.2)
plt.fill_between(x_07, a_in_integral_07, alpha=0.1)
plt.legend(['b=0.3', 'b=0.5', 'b=0.7'])
plt.xlabel('x')
plt.ylabel('a')
plt.subplot(1, 2, 2)

b = np.linspace(0.01, 0.99, 100)


def int_a(b):
    return integrate.quad(lambda x: b * (exp(-x) - exp(-(1 - b) * x)) / (1 - exp(-x)), 0, 1 / b)[0]


plt.plot(b, [int_a(i) for i in b])

plt.xlabel('b')
plt.ylabel('a')

plt.show()
