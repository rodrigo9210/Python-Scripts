# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:17:42 2019

@author: Rodrigo
"""

import numpy as np
import matplotlib.pyplot as plt

w = 2 #frecuencia
N = 10000
fs = 250
#genera un arreglo de 1x2500
t = np.linspace(0,10,fs*10)[np.newaxis,:]
print(t.shape) #para ver las dimensiones de t
#genera una lista desde 0 hasta 39 solo impares y agrega una dimension como en t
x = np.arange(40)[1::2, np.newaxis]
print(x.shape)
R = w * np.dot(x,t)
print(R.shape)
S = np.sin(R)
print(S.shape)
S = np.dot((1/x).T, S)
print(S.shape)
plt.plot(t.T, S.T)
plt.show()