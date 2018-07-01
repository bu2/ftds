# %%

import sys
sys.version


# %%

import matplotlib.pyplot as plt
import numpy


# %%

x = numpy.arange(360 * 5) / 360.0 * 2 * numpy.pi
y = numpy.sin(x)

(x, y)


# %%

plt.figure(figsize=(12, 8))
plt.plot(x, y)
plt.show()
