import numpy as np
import matplotlib.pylab as plt

## Almacene los datos de signal.dat y de incompletos.dat ##

signal= np.genfromtxt('signal.dat');
incompletos= np.genfromtxt('incompletos.dat');

##Haga una grafica de los datos de signal.dat y guarde dicha grafica sin mostrarla ApellidoNombre_signal.pdf ##

plt.plot(signal)
plt.xlabel('Tiempo');
plt.savefig("RozoDaniel_signal.pdf");

## Haga  la  transformada  de  Fourier  de  los  datos  de  la  senal  usando  su implementacion propia de la transformada discreta de fourier ##

def tdf(y,N,dt):
 n=np.arange(-N/2,N/2); 
 k=n.reshape((N,1)); 
 ft=np.exp(-2j * np.pi * k * n/(N+0.0));
 g=np.dot(ft,y);
 frec=n/(N*dt);
 return  np.transpose((frec,g))

dt=signal[-1,0]/(0.0+np.size(signal))
tf=tdf(signal[:,2],np.shape(signal)[0],dt);

## Haga una grafica de la transformada de Fourier y guarde dicha grafica sin mostrarla en ApellidoNombre_TF.pdf ##

fig_2=plt.figure()
plt.plot(tf[:,0],np.abs(tf[:,1]))
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.savefig("RozoDaniel_TF.pdf",dpi=fig_2.dpi);
print "No se utilizo el paquete fftfreq"

## Imprima un mensaje donde indique cuales son las frecuencias principales de su senal ##








