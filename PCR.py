import numpy as np
import matplotlib.pylab as plt

## Almacene los datos del archivo WDBC.dat ##
datos_r=np.genfromtxt('WDBC.dat', delimiter=',')[:,2:];
diagnostico=np.genfromtxt('WDBC.dat',usecols=[1], delimiter=',', dtype=None);

## Calcule, con su implementacion propia, la matriz de covarianza de los datos y la imprima ##

datos=np.copy(datos_r)
filas=np.size(datos[:,0]);
col=np.size(datos[0,:]);

for i in range(0,col):
 datos[:,i]=datos[:,i]-np.mean(datos[:,i])

sigma=np.zeros((col,col))
for i in range(0,col):
 for j in range (0,col):
  sigma[i,j]=np.sum(datos[:,i]*datos[:,j])/(filas-1);
 
print 'la matriz de covarianza es:' 
print sigma 

## Calcule los autovalores y autovectores de la matriz de covarianza y los imprima para esto puede usar los paquetes de linalg de numpy. Su mensaje debe indicar explicitamente cual es cada autovector y su autovalor correspondiente. ##

eigenval, eigenvec=np.linalg.eig(sigma)
for i in range(0,col):
 print 'el autovector para el autovalor ',eigenval[i], ' es: ', eigenvec[i,:]

## imprima un mensaje que diga cuales son los parametros mas importantes en base a las componentes de los autovectores ##

print  'los parametros mas importantes son el 1 y el 2'

## Haga una proyeccion de sus datos en el sistema de coordenadas PC1, PC2 y grafique estos datos.  Use un color distinto para el diagnostico maligno y el benigno y la guarde dicha grafica sin mostrarla en ApellidoNombre_PCA.pdf ##


benignos=np.where(diagnostico=='B');
malignos=np.where(diagnostico=='M');

proyeccion_1_benignos=np.matmul(datos_r[benignos,:], eigenvec[0,:])/np.linalg.norm(eigenvec[0])
proyeccion_2_benignos=np.matmul(datos_r[benignos,:], eigenvec[1,:])/np.linalg.norm(eigenvec[1])
proyeccion_1_malignos=np.matmul(datos_r[malignos,:], eigenvec[0,:])/np.linalg.norm(eigenvec[0])
proyeccion_2_malignos=np.matmul(datos_r[malignos,:], eigenvec[1,:])/np.linalg.norm(eigenvec[1])

fig_1=plt.figure()
plt.scatter(proyeccion_1_benignos,proyeccion_2_benignos);
plt.scatter(proyeccion_1_malignos,proyeccion_2_malignos);
plt.legend(['Benigno','Maligno'])
plt.xlabel('Componente 1');
plt.ylabel('Componente 2');
fig_1.suptitle('Proyeccion 1 vs 2')
fig_1.savefig('RozoDaniel_PCA.pdf');

