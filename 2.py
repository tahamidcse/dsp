import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 1, 0.01)
x = np.sin(2 * np.pi * 50 * t)

plt.figure(figsize=(12, 6))

plt.subplot(4, 2, 1)
plt.plot(t, x)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.50t)')
fs = 100
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 50 * n)
plt.subplot(4, 2, 2)
plt.stem(n, x_n)
plt.title("nyquist")
fs = 120
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 50 * n)
plt.subplot(4, 2, 3)
plt.stem(n, x_n)
plt.title("over sample")
fs = 80
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 50 * n)
plt.subplot(4, 2, 4)
plt.stem(n, x_n)
plt.title("undersample")
t = np.arange(0, 1, 0.001)
x = np.sin(2 * np.pi * 50 * t)

plt.subplot(4, 2, 5)
plt.plot(t, x)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.50t)')

fs = 40
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 10 * n)

plt.subplot(4, 2, 6)
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n) = sin(2π.(10/40)n)')

fs = 40
n = np.arange(0, 1, 1/fs)
x_n = np.sin(2 * np.pi * 50 * n)

plt.subplot(4, 2, 7)
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n) = sin(2π.(50/40)n) alias of 10hz')

plt.tight_layout()
plt.show()
