import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n >= 0 , 1 , 0)

def sine(f1 , t):
    return np.sin(2 * np.pi * f1 * t)

def coss(f1 , t):
    return np.cos(2 *np.pi * f1 * t)

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


     

n = np.arange(0,10,1)
#define parameters
x=unit_step(n)
h=unit_step(n)-unit_step(n-5)


plt.figure(figsize=(12,8))

plt.subplot(2, 2, 1)
plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n)')

plt.subplot(2, 2, 2)
plt.stem(n,h)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('h(n)')

# Convolution
y = convolve(x, h)

plt.subplot(2, 2, 3)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n) = x(n) * h(n)')
plt.tight_layout()
plt.show()