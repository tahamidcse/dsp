import numpy as np
import matplotlib.pyplot as plt

def unit_step_signal(n):
    return np.where(n >= 0 , 1 , 0)

def ramp_signal(n):
    return np.where(n >= 0 , n , 0)

def exponential_signal(a,n):
    return pow(a,n)

def sine_signal(f1 , t):
    return np.sin(2 * np.pi * f1 * t)

def cosine_signal(f1 , t):
    return np.cos(2 *np.pi * f1 * t)

#define parameters
n = np.arange(-10,10,1)

step_signal = unit_step_signal(n)
ramp = ramp_signal(n)
exponential = exponential_signal(1.5,n)


plt.figure(figsize=(12,8))

plt.subplot(3,2,1)
plt.stem(n,step_signal)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Unit Step Signal")

plt.subplot(3,2,2)
plt.stem(n,ramp)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Unit Ramp Signal")

plt.subplot(3, 2, 3)
plt.stem(n, exponential)
plt.title("Exponential Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()