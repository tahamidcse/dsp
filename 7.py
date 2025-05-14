import numpy as np
import matplotlib.pyplot as plt


     

def convolve(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    y = [0] * len_y

    for i in range(len_y):
        for k in range(len_x):
            if(i - k >= 0 and i - k < len_h):
                y[i] += x[k] * h[i - k]
    
    return y


     

x = [1, 3, -2, 4]
y = [2, 3, -1, 3]
z = [2, -1, 4, -2]
#h = [1, -1, 2, -2, 4, 1, -2, 5]

plt.figure(figsize=(7, 5))

plt.subplot(3, 2, 1)
plt.stem(x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n)')

plt.subplot(3, 2, 2)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n)')

plt.subplot(3, 2, 3)
plt.stem(z)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('z(n)')

# Crosscorrelation
yn = convolve(x, y[::-1])

plt.subplot(3, 2, 4)
plt.stem(yn)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('yn(n) = x(n) . y(n)')
yn = convolve(y, z[::-1])

plt.subplot(3, 2, 5)
plt.stem(yn)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('yn(n) = y(n) . z(n)')

plt.tight_layout()
plt.show()