# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:50:54 2019

@author: Rodrigo
"""
import numpy as np
import matplotlib.pyplot as plt

"""
x = np.array([0.7, 2.7, -0.5, -8.9, 2, 0, -3.7])
mascara = x<0
print(mascara)
print(x[mascara])
"""

nums = np.random.normal(0,1,1000) #media, varianza, num muestras
m0 = nums > -0.25
m1 = nums < 0.25
mascara = np.logical_and(m0,m1)
x = np.linspace(-1,1,1000)
print(nums[mascara])
plt.plot(x,nums)
plt.plot(x[mascara],nums[mascara],".")
plt.show()
