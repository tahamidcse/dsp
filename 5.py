import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
def  sin(a,f,v):
    return a*np.sin(2 * np.pi * f * v)
def  cos(a,f,v):
    return a*np.cos(2 * np.pi * f * v)
def arrange(v,fs):
    return np.arange(0,v,1/fs)


def signal(t):
    x1=cos(3,100,t)
    x2=sin(5,300,t)
    x3=cos(10,600,t)
    return x1+x2+x3



#add title labels

t=arrange(0.008,100000)
xt=signal(t)
plt.figure(figsize=(12,6))
plt.subplot(3,2,1)
plt.plot(t,xt)

fs=1200#......nyquist
n=arrange(0.008,fs)

xn=signal(n)

plt.subplot(3,2,2)
plt.plot(n,xn)
fs=900 #......undersample
n=arrange(0.008,fs)
xn=signal(n)
plt.subplot(3,2,3)
plt.plot(n,xn)

fs=1400 #......oversample
n=arrange(0.008,fs)
xn=signal(n)
plt.subplot(3,2,4)
plt.plot(n,xn)



plt.tight_layout()
plt.show()