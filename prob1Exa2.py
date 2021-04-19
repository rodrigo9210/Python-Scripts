# -*- coding: utf-8 -*-
"""
Problema 1 - Examen 2

@author: Rodrigo Arce
"""
import numpy as np

def evaluaFuncion(m_i,gamma,x,x_i):
    """evaluaFuncion con los valores de los parametros
        Params
        ------
            m_i:[]
                arreglo de dimension n
            gamma: float
                numero real que debe ser mayor que cero
            x:[]
                arreglo de dimension m
            x_i:[]
                arreglo de dimension n x m
        Return
        ------
            tipos:[]
                arreglo con el tipo de dato de cada dato del parametro datos
    """
    suma = 0
    
    for i in m_i:
        i = i - 1
        #print("---------------------------------")
        #print("I: " , i) 
        fila = x_i[i]
        #print("fila x_i: ",fila)
        resta = np.subtract(x, fila)
        #print("resta: ",resta)
        prod = np.dot(resta,resta)
        #print("prod punto: ", prod)
        gam = gamma * prod
        #print("gam: ",gam)
        exp = np.exp(gam)
        #print("exp: ",exp)
        #print("m_i[i] ",m_i[i])
        mult = m_i[i] * exp
        #print("mult: ",mult)
        suma = suma + mult
        #print("suma: ",suma)
    
    return suma
    

def main():
    m_i   = np.array([1, 2, 3])
    gamma = 2
    x_i   = np.array([[1,2,3,4,5],
            [2,3,4,5,6],
            [3,4,5,6,7]])
    x     = np.array([1, 2, 3, 4, 5])
    
    if (gamma < 0):
        print("Gamma es menor que 0.")
    elif len(x) != len(x_i[0]):
        print("El num de columnas de x & x_i no coinciden.")
    elif len(x_i) != len(m_i):
        print("El numero de filas de x_i no coincide con el num de columnas de m_i")
    else:
        print("El resultado es: ", evaluaFuncion(m_i,gamma,x,x_i))

if __name__ == "__main__":
    main()