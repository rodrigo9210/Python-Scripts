# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:49:56 2019

@author: Rodrigo
"""
import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the walk
dims = 2
step_n = 10000
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))


# Simulate steps in 2D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
average1 = np.average(path[:,0])
average2 = np.average(path[:,1])
print('PROMEDIO: ', average1,', ', average2)
sum1 = np.sum(path[:,0])
sum2 = np.sum(path[:,1])
print('SUMA: ', sum1,', ', sum2)
start = path[:1]
stop = path[-1:]


# Plot the path
fig = plt.figure(figsize=(8,8),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(path[:,0], path[:,1],c='blue',alpha=0.25,s=0.05);
ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.25,ls='-');
ax.plot(start[:,0], start[:,1],c='red', marker='+')
ax.plot(stop[:,0], stop[:,1],c='black', marker='o')
ax.plot(average1, average2, c='green', marker='s')
plt.title('2D Random Walk')
plt.tight_layout(pad=0)
#plt.savefig('plots/random_walk_2d.png',dpi=250);

