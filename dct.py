import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------
# 1D DCT (Type-II)
# ----------------------------------------
def DCT_1D(x, N):
    X = np.zeros(N)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.cos(np.pi * (n + 0.5) * k / N)
    return X

# ----------------------------------------
# Inverse DCT (Type-III)
# ----------------------------------------
def IDCT_1D(X, N):
    x = np.zeros(N)
    for n in range(N):
        x[n] = X[0] / 2
        for k in range(1, N):
            x[n] += X[k] * np.cos(np.pi * (n + 0.5) * k / N)
    x *= 2 / N
    return x

# ----------------------------------------
# Test Signal
# ----------------------------------------
f1 = 1000
f2 = 2000
fs = 8000
T = 1 / fs
N = 8

n = np.arange(N)
phase_shift = 3 * np.pi + 4

xn = np.sin(2 * np.pi * f1 * n * T) + 0.5 * np.sin(2 * np.pi * f2 * n * T + phase_shift)

# Compute DCT and inverse DCT
Xdct = DCT_1D(xn, N)
x_idct = IDCT_1D(Xdct, N)

# ----------------------------------------
# Display
# ----------------------------------------
print("x(n):")
print(xn)
print("\nDCT coefficients:")
print(Xdct)
print("\nReconstructed x(n) from IDCT:")
print(x_idct)

# ----------------------------------------
# Plots
# ----------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, xn)
plt.title("Original Signal x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, Xdct)
plt.title("DCT Coefficients")
plt.xlabel("Frequency index k")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, x_idct)
plt.title("Reconstructed Signal using IDCT")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
