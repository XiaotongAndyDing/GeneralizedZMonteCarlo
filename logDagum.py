import scipy.special
import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(0.01, 1, 100)
digamma = scipy.special.digamma(1 - b) - scipy.special.digamma(1)

# b = 0.5
# dagum = -b * np.log(np.power(np.random.rand(1000), 1 / (b - 1)) - 1)

dagum_list = np.array([np.mean(-b * np.log(np.power(np.random.rand(10000), 1 / (b - 1)) - 1)) for b in
              np.linspace(0.01, 1, 100)])

plt.plot(b[:-2], digamma[:-2], b, dagum_list, 'x')
plt.xlabel('b')
plt.ylabel('Expectation')
plt.title('Expectation of Log-Dagum scale volatility to 1')
plt.legend(['Theoretical value', 'Monte Carlo by 10000 paths'])
plt.show()

# plt.hist(dagum)
# plt.show()

end = None
