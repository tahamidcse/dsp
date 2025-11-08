import numpy as np
import matplotlib.pyplot as plt

def _DFT(x , N):
    result = np.zeros(N , dtype=complex)

    for m in range(N):
        for n in range(N):
            result[m] += x[n] * np.exp(-1j * 2 * np.pi * m * n / N)
    
    return result

def _IDFT(dft,N):
    result = np.zeros(N)

    for n in range(N):
        for m in range(N):
            result[n] += dft[m] * np.exp(1j * 2 * np.pi * m * n / N)
    result /= N
    
    return result
    


f1 = 1000
f2 = 2000
fs = 8000
T = 1/fs

phase_shift = 3 * np.pi + 4
N = 8 #number of samples

n = np.arange(N)

xn = np.sin(2 * np.pi * f1 * n * T) + 0.5 * np.sin(2 * np.pi * f2 * n * T + phase_shift)

dft = _DFT(xn, N)
idft = _IDFT(dft, N)

magnitude = np.abs(dft)
phase = np.angle(dft , deg=True)
real_part = np.real(dft)
imaginary_part = np.imag(dft)

threshold = 1e-10

#applying threshold values to small values
magnitude = np.where(magnitude < threshold , 0 , magnitude)
phase = np.where(np.abs(phase) < threshold , 0 , phase)
real_part = np.where(np.abs(real_part) < threshold , 0 , real_part)
imaginary_part = np.where(np.abs(imaginary_part) < threshold , 0 , imaginary_part)

print("Values of xn")
for i in range(N):
    print(xn[i])
print("DFT values")
for i in range(N):
    print(dft[i])

print("IDFT values")
for i in range(N):
    print(idft[i])

print("Real part")
for i in range(N):
    print(real_part[i])

print("Imaginary part")
for i in range(N):
    print(imaginary_part[i])

# Plotting
plt.figure(figsize=(12,8))

#plotting the original values of x(n)
plt.subplot(3,2,1)
plt.plot(n,xn)
plt.stem(n , xn , linefmt="green")
plt.title("Values of x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")

#plotting the magnitude of dft
plt.subplot(3,2,2)
plt.stem(n , magnitude)
plt.title("Magnitude of DFT")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)

#plotting the phase of dft
plt.subplot(3,2,3)
plt.stem(n , phase)
plt.title("Phase of DFT")
plt.xlabel("Frequency")
plt.ylabel("Phase")
plt.grid(True)

#plotting the realpart
plt.subplot(3,2,4)
plt.stem(n , real_part)
plt.title("Real part")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)

#plotting the imaginary part
plt.subplot(3,2,5)
plt.stem(n , imaginary_part)
plt.title("imaginary part")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)

#plotting the original values of x(n)
plt.subplot(3,2,6)
plt.stem(n , idft)
plt.title("Values of idft")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
