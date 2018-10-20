from PIL import Image
import numpy as np
import matplotlib.pylab as plt 
from scipy.fftpack import fft2, ifft2

# Almacene la imagen arbol.png en una arreglo de numpy #
imagen= plt.imread('arbol.png');
data_imagen=np.asarray(imagen);

# Usando los paquetes de scipy, realice la transformada de Fourier de la imagen.  Eligiendo una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en ApellidoNombre_FT2D.pdf #

ft_imagen=fft2(data_imagen);
ft_imagen=np.fft.fftshift(ft_imagen);
ft_imagen=np.log(np.abs(ft_imagen));
lowest = np.nanmin(ft_imagen[np.isfinite(ft_imagen)])
highest = np.nanmax(ft_imagen[np.isfinite(ft_imagen)])
original_range = highest - lowest
norm_f = (ft_imagen - lowest) / original_range 

fig_1=plt.figure()
plt.imshow(norm_f);
fig_1.savefig("RozoDaniel_FT2D.pdf");




