from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import ifft, ifftshift

from mpl_toolkits.mplot3d import Axes3D

# hf = plt.figure()
# ha = hf.add_subplot(111, projection='3d')


def char_function(t, b, T=1, n=500, freq_space=100):
    assert 0 < b <= 1
    z = np.linspace(-freq_space, 0, n // 2)
    res_1 = gamma(1 - b + b * z * 1j) * gamma(1 - b * z * 1j) / gamma(1 - b)
    part1 = np.power(res_1, t / T)
    z = np.linspace(0, freq_space, n // 2)
    res_1 = gamma(1 - b + b * z * 1j) * gamma(1 - b * z * 1j) / gamma(1 - b)
    part2 = np.power(res_1, t / T)
    res = np.append(part2, part1)
    return res


def z_pdf_function(b, n=500):
    x = np.linspace(-10, 10, n)
    return ((1 - b) / b) * np.exp(x * ((1 - b) / b)) / np.power(1 + np.exp(x / b), 2 - b)


def pdf_generalized_z(t, b, T=1, n=500, freq_space=100):
    return ifftshift(ifft(char_function(t, b, T, n, freq_space)))


# t = np.linspace(0.1, 1, 500)
# x = np.linspace(-5, 5, 500)
#
# X, Y = np.meshgrid(x, t)
#
# plot_z = np.array([pdf_generalized_z(i, 0.5).real for i in t]).reshape(len(t), len(x))
#
# ha.plot_surface(X, Y, plot_z, antialiased=False, alpha=0.1, color='b')
# plt.xlabel('x')
# plt.ylabel('time')
# ha.set_zlabel('probability density')
# ha.set_xlim(-2, 2)


plt.plot(np.linspace(-5, 5, 500), pdf_generalized_z(0.3, 0.5))
plt.plot(np.linspace(-5, 5, 500), pdf_generalized_z(0.5, 0.5))
plt.plot(np.linspace(-5, 5, 500), pdf_generalized_z(0.7, 0.5))
plt.plot(np.linspace(-5, 5, 500), pdf_generalized_z(1, 0.5))
plt.legend(['0.3', '0.5', '0.7', '1'])
plt.xlim(-2.5, 2.5)
plt.xlabel('x')
plt.ylabel('probability density')

plt.show()


end = None
