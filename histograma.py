# -*- coding: utf-8 -*-
"""
HISTOGRAMA

@author: Rodrigo
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 9, 12, 11, 3, 14, 1, 20, 8, 17, 17, 1, 10, 19, 5 ,2])

#1 crear numero de grupos equiespaciados(min(x)-1, max(x)+1, N)
# ej si (0, 21, N=5), [0, 5.25, 10.5, 15.75, 21]
bins = np.linspace(x.min()-1, x.max()+1, 5)

#2 transponer x como vector columna (x.T) tal que su dimension es Nx1 para poder manejarlo con mascaras
x = x[:,np.newaxis]

#3 agrupar datos de x.T de la forma: (x > bins[0:end-1]) and (x < bins[1:end]), dimension = NxK
c = (x > bins[:-1]) * (x < bins[1:])

#4 sumar(c, ejes = K)
L = c.sum(axis = 0)

#5 graficar calculando todas las diferencias posibles
plt.bar(bins[1:]/2, L, np.diff(bins)[0] * 0.4)
plt.show()

#6 comparar con funcion histograma
plt.hist(x, bins=4)