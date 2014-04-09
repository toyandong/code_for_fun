import matplotlib.pyplot as plt
import numpy as np
import sys

x=np.linspace(-10,10)
plt.plot(x, 1-x, '-', color='r',label='y=1-x')
plt.axvline(x=0,color='b')
plt.axhline(y=0, color='k')
plt.plot(x, x-1, '-', color='g',label='y=x-1')

plt.show()

















