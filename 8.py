import numpy as np
import matplotlib.pyplot as plt
def unitstep(n):
  return np.where(n>=0,1,0)
def coss(f,v):
  return np.cos(f*v)
n=np.arange(0,120)
x1=np.zeros_like(n,dtype=float)
x1[n>=20]=1
x2=coss(np.pi/8,n)
x3=coss(7*np.pi/8,n)
ha=[1/6,1/6,1/6,1/6,1/6,1/6]
hd=[1/6,-1/6,1/6,-1/6,1/6,-1/6]
y1=np.convolve(x1,h,mode='same')
yd1=np.convolve(x1,hd,mode='same')
y2=np.convolve(x2,h,mode='same')
yd2=np.convolve(x2,hd,mode='same')
y3=np.convolve(x3,h,mode='same')
yd3=np.convolve(x3,hd,mode='same')
plt.figure(figsize=(12,6))
plt.subplot(3,2,1)

plt.stem(n,y1)
plt.plot(n,y1)
plt.subplot(3,2,2)

plt.stem(n,yd1)
plt.plot(n,yd1)
plt.subplot(3,2,3)
plt.stem(n,y2)
plt.plot(n,y2)
plt.subplot(3,2,4)
plt.stem(n,yd2)
plt.plot(n,yd2)
plt.subplot(3,2,5)
plt.stem(n,y3)
plt.plot(n,y3)
plt.subplot(3,2,6)
plt.stem(n,yd3)
plt.plot(n,yd3)

plt.tight_layout()
plt.show()