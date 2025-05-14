import numpy as np
import matplotlib.pyplot as plt
omega =[0,np.pi/4,np.pi/2]

n=np.arange(0,40)
plt.figure(figsize=(10,6))
for i in range (len(omega)):
  x=np.cos(omega[i]*n)
  plt.subplot(2,2,i+1)
  plt.stem(x)