# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:18:32 2019
                        REAL
              Clase 1         Clase 2
        ------------------------------------
E    C1  | TRUE POSITIVE  | FALSE POSITIVE |
S         -----------------------------------
T    C2  | FALSE NEGATIVE | TRUE NEGATIVE  |
        ------------------------------------
@author: Rodrigo
"""

import numpy as np

x = np.ones(100)
x[:50] = -1

I = np.arange(x.shape[0]) # 0,1,2,3...99

np.random.shuffle(I) #revuelve los indices
x_test = x[I] 
np.random.shuffle(I) #revuelve los indices
x_train = x[I]

TRUE_POS = x_test == -1
TP = np.sum(x_train[TRUE_POS] == -1)
TN = np.sum(x_train[~TRUE_POS] == 1)


TRUE_NEG = x_test == 1
FN = np.sum(x_train[TRUE_NEG] == -1)
FP = np.sum(x_train[~TRUE_NEG] == 1)

print("TRUE POS: ",TP)
print("TRUE NEG: ",TN)
print("FALSE NEG: ",FN)
print("FALSE POS: ",FP)

#accuracy = suma diagonales / suma total
#NO CONFIABLE EN CLASES DESVALANCEADAS
acc = (TP + TN) / (TP + TN + FP + FN)

print("ACCURACY: ", acc)

#sensibility = TP / (TP + FN) : tp sobre la suma de su columna
#buen clasificador: sens > 0.75
sen = TP / (TP + FN)
print("SENSIBILITY: ", sen)

#especifity = TN / (TN + FP) : tn sobre la suma de su columna
#buen clasificador: esp > 0.75
esp = TN / (TN + FP)
print("ESPECIFITY: ", esp)