import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import interp1d

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
plt.xlabel('Tiempo');
plt.ylabel('Magnitud');
plt.savefig("RozoDaniel_filtrada.pdf",dpi=fig_3.dpi);

#Escriba un mensaje en la terminal explicando por que no puede hacer la transformada de Fourier de los datos de incompletos.dat #
#fig=plt.figure()
#plt.plot(incompletos[:,0],incompletos[:,2]);
#plt.show()

# Haga una interpolacion cuadratica y una cubica de sus datos incompletos.dat con 512 puntos.  Haga la trasformada de Fourier de cada una de las series de datos interpoladas #

cuad=interp1d(incompletos[:,0],incompletos[:,2],kind='quadratic');
cub=interp1d(incompletos[:,0],incompletos[:,2],kind='cubic');

t=np.linspace(incompletos[0,0],incompletos[-1,0], num=512)
datos_cuad=cuad(t)
datos_cubic=cub(t)

tf_cuad=tdf(datos_cuad,np.shape(datos_cuad)[0],t[1]-t[0]);
tf_cub=tdf(datos_cubic,np.shape(datos_cuad)[0],t[1]-t[0]);

# Haga una grafica con tres subplots de las tres transformada de Fourier (datos de signal.dat y datos interpolados) y guardela sin mostrarla en ApellidoNombre_TF_interpola.pdf #

tf=tdf(signal[:,2],np.shape(signal)[0],dt);

fig_4=plt.figure()
plt.subplot(1,3,1)
plt.plot(tf[:,0],np.abs(tf[:,1]));
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.title("senal")
plt.subplot(1,3,2)
plt.plot(tf_cuad[:,0],np.abs(tf_cuad[:,1]));
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.title("Cuadratica")
plt.subplot(1,3,3)
plt.plot(tf_cub[:,0],np.abs(tf_cub[:,1]));
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.title("Cubica")
plt.savefig("RozoDaniel_TF_interpola.pdf",dpi=fig_4.dpi);

# Imprima un mensaje donde describa las diferencias encontradas entre la transformada deFourier de la senal original y las de las interpolaciones #


#Aplique el filtro pasabajos con una frecuencia de corte fc=1000 Hz y con una frecuencia de corte de fc=500Hz#

def filtro_pasabajos(arr,fc):
 arr_fil=arr.copy()
 arr_fil[np.where(np.abs(arr_fil[:,0])>fc),1]=0;
 return arr_fil

tf_fil_1000=filtro_pasabajos(tf,1000)
tf_cuad_fil_1000=filtro_pasabajos(tf_cuad,1000);
tf_cub_fil_1000=filtro_pasabajos(tf_cub,1000);
tf_fil_500=filtro_pasabajos(tf,500)
tf_cuad_fil_500=filtro_pasabajos(tf_cuad,500);
tf_cub_fil_500=filtro_pasabajos(tf_cub,500);

# Haga una grafica con dos subplots (uno para cada filtro) de las 3 senales filtradas y guardela sin mostrarla en ApellidoNombre_2Filtros.pdf #

fig_5=plt.figure()
plt.subplot(2,1,1)
plt.plot(tf_fil_1000[:,0],tf_fil_1000[:,1],tf_cuad_fil_1000[:,0],tf_cuad_fil_1000[:,1]
,tf_cub_fil_1000[:,0],tf_cub_fil_1000[:,1])
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.title("Fc=1000Hz");
plt.xlim(-1500,1500);
plt.subplot(2,1,2)
plt.plot(tf_fil_500[:,0],tf_fil_500[:,1],tf_cuad_fil_500[:,0],tf_cuad_fil_500[:,1]
,tf_cub_fil_500[:,0],tf_cub_fil_500[:,1])
plt.xlabel('Frecuencia');
plt.ylabel('Magnitud');
plt.title("Fc=500Hz");
plt.xlim(-1000,1000);
plt.savefig("RozoDaniel_2Filtros.pdf",dpi=fig_5.dpi);





 






