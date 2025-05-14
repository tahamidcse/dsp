import numpy as np
import matplotlib.pyplot as plt



t = np.arange(0, 1, 0.001)
x = 3*np.cos(2 * np.pi * 50 * t)

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(t, x)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('x(t) = 3cos(2π.50t)')



fs = 200
n = np.arange(0, 1, 1/fs)
x = 3*np.cos(2 * np.pi * 50 * n)

plt.subplot(2, 2, 2)
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('200hz)')
fs = 75
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 50 * n)

plt.subplot(2, 2, 3)
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('fs=75')


plt.tight_layout()
plt.show()