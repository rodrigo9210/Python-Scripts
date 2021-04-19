# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:20:37 2019

@author: Rodrigo
"""

import pandas as pd
import numpy as np


def iris():
    #1. abrir IRIS
    
    #lee datos
    data = pd.read_csv('iris.csv')
    
    #2. seleccionar ('setosa', 'virginica') -> x,y
    
    #obten todos los que la columna variety sea diferente de versicolor
    Set = data.loc[data.variety!='Versicolor']
    #obten estas 4 columnas para todos los que no sean versicolor
    X = data.loc[:,['sepal.length','petal.length','sepal.width','petal.width']][data.variety!='Versicolor']
    #obten la columna variety para todos los que no sean versicolor
    Y = data.loc[:,['variety']][data.variety!='Versicolor']
    #genera un arreglo de unos con el numero de filas de Y
    L = np.ones(Y.shape[0])
    #usa Y como mascara para cambiar el valor en L en los casos iguales a setosa
    L[Y.variety=='Setosa'] = -1
    
    return X, Y, L

#3. separar (x,y) -> X_train, Y_train, X_eval, Y_eval
def separar(X, Y, L):
    #divide datos para entramiento y para prueba (40 entramiento, 10 prueba)
    X_Train = np.concatenate((X.values[:40],X.values[50:-10]), axis = 0)
    Y_Train = np.concatenate((L[:40],L[50:-10]), axis = 0)
    X_Test = np.concatenate((X.values[40:50],X.values[-10:]), axis = 0)
    Y_Test = np.concatenate((L[40:50],L[-10:]), axis = 0)
    return X_Train, Y_Train, X_Test, Y_Test

#4. generar vias -> mascaras con dos matrices identidades concatenadas multiplicadas por vector de unos [I I]*[11111111]
def mascaras():
    #1. generar matriz identidad
    I1 = np.identity(5)
    I2 = np.identity(5)
    I = np.concatenate(I1, I2)
    
    #2. Matriz para multiplicar
    B = np.ones(8)
    
    #3. hacer mascara del producto kroncecker: == 0 para datos de entrenamiento (80%), == 1 para datos de prueba (20%)
    M = np.kron(I,B) == 0
    
    return M

#5. para cada viaz: entrena(X_TN, Y_TN), evalua(X_TS, Y_TS) -> sensibilidad(i), especificidad(i)
def entrena(X_TN, Y_TN, M):
    #ENTRENAR = REGRESION LINEAL "LINEAR DISCRIMINAT ANALYSIS (LDA)"
    W = np.linalg.pinv(X_TN)
    W = np.dot(W, Y_TN)
    
    E = np.dot(W[np.newaxis], X_TS.T)
    #genera una mascara con los datos de E que solo tenga valores: 1 y -1
    E = -2 * (E<0) + 1
    
    return E
    
def evalua(X_TS, Y_TS):
    

#6. promedio(sensibilidad, especificidad), std(sensibilidad, especificidad)