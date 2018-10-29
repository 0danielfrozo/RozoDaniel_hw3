import numpy as np
import matplotlib.pylab as plt

## Almacene los datos del archivo WDBC.dat ##
datos =np.genfromtxt('WDBC.dat', delimiter=',')[:,2:];

## Calcule, con su implementacion propia, la matriz de covarianza de los datos y la imprima ##

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

## Calcule los autovalores y autovectores de la matriz de covarianza y los imprima (para esto puede usar los paquetes de linalg de numpy).  Su mensaje debe indicar expıcitamente cual es cada autovector y su autovalor correspondiente. ##

eigenval, eigenvec=np.linalg.eig(sigma)
print 'autovalores:', eigenval
print 'autovectores:',eigenvec


