import numpy as np
import matplotlib.pylab as plt

## Almacene los datos de signal.dat y de incompletos.dat ##

signal= np.genfromtxt('signal.dat');
incompletos= np.genfromtxt('incompletos.dat');

##Haga una grafica de los datos de signal.dat y guarde dicha grafica sin mostrarla ApellidoNombre_signal.pdf ##

plt.plot(signal[:,0],signal[:,2])
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

print "Las frecuencias principales de la senal son: "
frec_principales=tf[np.where(np.abs(tf[:,1])>300),0];
print np.abs(frec_principales[np.where(frec_principales>0)])

## Haga un filtro pasa bajos con frecuencia de corte fc=1000 Hz. realice la transformada inversa y haga una grafica de la senal filtrada. Guarde dicha grafica son mostrarla en ApellidoNombre_filtrada.pdf ## 


tf[np.where(np.abs(tf[:,0])>1000),1]=0;

def ift(g,N):
 n=np.arange(-N/2,N/2); 
 k=n.reshape((N,1)); 
 ft=np.exp(2j * np.pi * k * n/(N+0.0));
 y=1/(N+0.0)*np.dot(ft,g);
 return  y

senal_filt=ift(tf[:,1],np.shape(tf)[0]);
fig_3=plt.figure()
plt.plot(signal[:,0],senal_filt)
plt.plot(signal[:,0],signal[:,2])
plt.xlabel('Tiempo');
plt.ylabel('Magnitud');
plt.savefig("RozoDaniel_filtrada.pdf",dpi=fig_3.dpi);


 



