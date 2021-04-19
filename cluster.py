# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:38:45 2019

@author: Rodrigo
"""

###### K-means (Lloyd)

#1. elegir aleatoriamente un num de k centroides

#2. calcular las distancias de cada punto (xi) a cada centroide (ci) (distancia euclidania, manhattan, mahalanobis)

#para 50 puntos y 2 centroides
#d = xi - c: (50,2)
#d = d^2 para que sean positivas: (50,2)

#3. min(d,c) : (50,2)

#4. funcion de pertenencia : 1 si xi pertenece a ci, 0 otro caso

import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

N = 300
rd = 150

x,y = make_blobs(n_samples = N, random_state = rd)

plt.plot(x[y==0,0], x[y==0,1], 'ro')
plt.plot(x[y==1,0], x[y==1,1], 'bo')
plt.plot(x[y==2,0], x[y==2,1], 'go')

k = 3
#crea tres clusters degenerados de dos dimensiones
c = np.random.normal(1,5,(k,2))
#agrupa filas y columnas de centroides
plt.plot(c[:,0],c[:,1],'ko')


d = x[:,:,np.newaxis] #(300,2,1)
d = d - c.T #(300,2,3) -> (elem, componentes, centroides)
d = np.power(d,2) #(300,2,3)
d = d.sum(axis = 1) #(300,3)

#tindica que columna es la menor de cada fila
d = np.argmin(d,axis = 1) # {0,1,2}: (300,1)

#saca la media para cada valor de x (cada fila) que pertence a su minimo correspondiente (mascara d)
for i in set(d):
    c[i] = x[d==i].mean(axis = 0)

plt.plot(c[:,0],c[:,1],'yo')

