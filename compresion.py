# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:15:37 2019

@author: Rodrigo
"""

import imageio as mio
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans as kmeans

ss = mio.imread('ss.jpg')
#submuestrea la imagen cada 10 pixeles
ss_sub = ss[::10, ::10, :] #shape: (75, 60, 3)

plt.imshow(ss_sub)
plt.show()

s = ss_sub.shape
#generar ambiente 3d (xyz -> RGB)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')



#espaguetizar cada color y mostrar su color original en la gráfica
ax.scatter(ss_sub[:,:,0].ravel(),
           ss_sub[:,:,1].ravel(),
           ss_sub[:,:,2].ravel(),
           c = ss_sub.reshape(s[0] * s[1], s[-1])/256)

#rota la imagen: ax.view_init(50,20)

s = ss.shape
X_train = ss.reshape(s[0] * s[1], s[-1])
#separar informacion para que no itnerfieran entre si
ss_comp = X_train.copy()

#genera n cluesters
model = kmeans(n_clusters = 30)
#entrena: encuentra los centroides de cada cluster
model.fit(X_train)

#encuentra distancia de cada elemento a su cluster mas cercano
X_L = model.predict(X_train)

#regresa coordenadas de los centroides y lo bligamos a que sea int para el modelo RGB
cen = model.cluster_centers_.astype(int)

#toma cada centroide, ve los elementos mas cercanos a ese centroide y los sustituye por el centroide
for n,c in enumerate(cen):
    ss_comp[X_L == n] = c
    
plt.imshow(ss_comp.reshape(s))
plt.show()