import numpy as np
import matplotlib.pylab as plt 
from scipy.fftpack import fft2, ifft2

# Almacene la imagen arbol.png en una arreglo de numpy #
imagen= plt.imread('arbol.png');
data_imagen=np.asarray(imagen);

# Usando los paquetes de scipy, realice la transformada de Fourier de la imagen.  Eligiendo una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en ApellidoNombre_FT2D.pdf #

ft_imagen=fft2(data_imagen);
ft_imagen=np.fft.fftshift(ft_imagen);
ft_Log=np.log(np.abs(ft_imagen));

fig_1=plt.figure()
plt.imshow(ft_Log);
fig_1.savefig("RozoDaniel_FT2D.pdf");


# Haga un filtro que le permita eliminar el ruido periodico de la imagen.  Para esto haga pruebas de como debe modificar la transformada de Fourier #

filtrado=ft_imagen.copy()
filtrado[np.where(ft_Log>0.9 *np.max(ft_Log))]=1;
ft_Log=np.log(np.abs(filtrado));



#grafique la transformada  de  Fourier  despues del proceso de filtrado,  esta  vez en escala LogNorm y guarde dicha grafica sin mostrarla en ApellidoNombre_FT2D_filtrada.pdf#

fig_2=plt.figure()
plt.imshow(ft_Log);


# Haga la transformada de Fourier inversa y grafique la imagen filtrada.  Verifique que su filtro elimina el ruido periodico y guarde dicha imagen sin mostrarla en ApellidoNombre_Imagen_filtrada.pdf #


img_filt= np.abs(ifft2(filtrado))
fig_3=plt.figure()
plt.imshow(img_filt);
plt.show()
