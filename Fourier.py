import numpy as np
import matplotlib.pylab as plt

## Implemenacion propia TF ##
def tdf(y,N,dt):
n=np.arange(-N/2.0,N/2.0);
k=n.reshape((N,1));
ft=np.exp(-2j*np.pi*k*n/(N+0.0));
g=np.dot(ft*y);
frec=n/(N*dt);
return g, frec


## Almacene los datos de signal.dat y de incompletos.dat ##

signal= np.getfromtxt('signal.dat');
incompletos= np.getfromtxt('incompletos.dat');

plt.plot(signal)
plt.plot(incompletos)
plt.show()








