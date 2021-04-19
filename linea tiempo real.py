import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
 
def update_line(hl, new_data):
	xdata, ydata, zdata = hl._verts3d
	hl.set_xdata(list(np.append(xdata, new_data[0])))
	hl.set_ydata(list(np.append(ydata, new_data[1])))
	hl.set_3d_properties(list(np.append(zdata, new_data[2])))
	plt.draw()
 
map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)
 
# # # Setting the axes properties
map_ax.set_xlim3d([0.0, 10.0])
map_ax.set_ylim3d([0.0, 10.0])
map_ax.set_zlim3d([0.0, 10.0])
 
hl, = map_ax.plot3D([0], [0], [0])
 
update_line(hl, (2,2, 1))
plt.show(block=False)
plt.pause(1)
 
update_line(hl, (5,5, 5))
plt.show(block=False)
plt.pause(2)
 
update_line(hl, (8,1, 4))
plt.show(block=True)

##### ALTERNATIVA

"""
import numpy as np
from matplotlib import pyplot as plt

def main():
    plt.axis([-50,50,0,10000])
    plt.ion()
    plt.show()

    x = np.arange(-50, 51)
    for pow in range(1,5):   # plot x^1, x^2, ..., x^4
        y = [Xi**pow for Xi in x]
        plt.plot(x, y)
        plt.draw()
        plt.pause(0.001)
        input("Press [enter] to continue.")

if __name__ == '__main__':
    main()

"""