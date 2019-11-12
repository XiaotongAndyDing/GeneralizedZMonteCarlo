import matplotlib.pyplot as plt
import numpy as np

x_n = np.linspace(-5, -0.2, 500)
x_p = np.linspace(0.2, 5, 500)
b = 0.5

v_p = [np.exp(-i / b) / (i * (1 - np.exp(-i / b))) for i in x_p]
v_n = [np.exp(i * (1 - b) / b) / ((-i) * (1 - np.exp(i / b))) for i in x_n]

plt.subplot(1, 2, 1)
plt.plot(x_n, v_n, x_p, v_p, -x_p, v_p)
plt.ylim((0, 1.25))
plt.legend(['v<0', 'v>0', 'v<0 reflection by y'])
plt.xlabel('x')
plt.ylabel('v')
plt.subplot(1, 2, 2)
b = 0.2
v_p_02 = [np.exp(-i / b) / (i * (1 - np.exp(-i / b))) for i in x_p]
v_n_02 = [np.exp(i * (1 - b) / b) / ((-i) * (1 - np.exp(i / b))) for i in x_n]
b = 0.5
v_p_05 = [np.exp(-i / b) / (i * (1 - np.exp(-i / b))) for i in x_p]
v_n_05 = [np.exp(i * (1 - b) / b) / ((-i) * (1 - np.exp(i / b))) for i in x_n]
b = 0.8
v_p_08 = [np.exp(-i / b) / (i * (1 - np.exp(-i / b))) for i in x_p]
v_n_08 = [np.exp(i * (1 - b) / b) / ((-i) * (1 - np.exp(i / b))) for i in x_n]
plt.plot(list(x_n)+list(x_p), v_n_02+v_p_02, list(x_n)+list(x_p), v_n_05+v_p_05, list(x_n)+list(x_p), v_n_08+v_p_08)
plt.ylim((0, 1.25))
plt.legend(['b=0.2', 'b=0.5', 'b=0.8'])
plt.xlabel('x')
plt.ylabel('v')
plt.show()
