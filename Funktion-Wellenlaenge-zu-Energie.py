import matplotlib.pyplot as plt
import numpy


wellenlaengen = numpy.arange(400,1200)
energie = 1.2398/wellenlaengen*1000

plt.xlabel("Wellenlänge in µm")
plt.ylabel("Energie in eV")
plt.plot(wellenlaengen, energie)
plt.show()