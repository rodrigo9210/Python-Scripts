# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:01:59 2019

@author: Rodrigo
"""

import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from scipy import signal
from scipy.misc import electrocardiogram

"""
elevationArray = [4411.94189453125,
             1658.561645507812,
             1085.295776367188,
             1491.4912109375,
             1583.762817382812,
             488.8834228515625,
             933.0382080078125,
             1657.123779296875,
             1074.835205078125,
             -84.51690673828125]

elevationArray = np.array(elevationArray)

peaks, _ = find_peaks(elevationArray)

plt.plot(elevationArray)
plt.plot(peaks, elevationArray[peaks], "x")
plt.show()
"""


#xs = np.arange(0, np.pi, 0.05)
data = electrocardiogram()[2000:4000]
peakind = signal.find_peaks_cwt(data, np.arange(1,120))
peakind, data[peakind]

plt.plot(data)
plt.plot(peakind, data[peakind], "x")
plt.show()
"""

import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np

x = electrocardiogram()[2000:4000]
peaks, _ = find_peaks(x, distance=150)
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()
"""