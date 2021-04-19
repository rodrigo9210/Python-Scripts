# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:31:48 2019

@author: Rodrigo
"""
import numpy as np
import matplotlib.pyplot as plt

#1 cargar archivo
c = ''
with open('bh.txt', 'r') as txt:
    for x in txt:
        c += x

#2 eliminar ' ', '\n', '\t'
c.replace(" ", "").replace('\n', "").replace('\t', "")

#3 separar las letras en un arreglo
c = np.array(list(c))

#4 obtener caracteres unicos
L = np.unique(c)
L = np.sort(L)

#5 suma coincidencias
S =  (c[:,np.newaxis] == L).sum(axis = 0)

line = np.arange(L.shape[0])
plt.hist(S)
plt.xticks(line, L)
