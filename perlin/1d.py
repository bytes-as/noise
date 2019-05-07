import math
import numpy
import matplotlib.pyplot

repeat = 5
slope = numpy.random.rand(repeat + 1)*2 -1
slope[repeat] = slope[0]
# for i in range(repeat):
#     slope[i] = numpy.random.rand()*2 - 1
def lerp(t , a, b):
    return a + t*(b-a)

def fade(t): 
    return t ** 3 * (t * (t * 6 - 15) + 10)
print(slope)
def perlin1D(point):
    point = point % repeat
    low = math.floor(point)
    low_slope = slope[low]
    high = low + 1
    high_slope = slope[high]
    distance = point - low
    low_position = low_slope * distance
    high_distance = high_slope * (distance - 1)
    return lerp(fade(distance), low_position, high_distance)

x = numpy.linspace(0, 10, 1000)
y = numpy.linspace(0, 10, 1000)
matplotlib.pyplot.plot(x, y, 'r')
# y = numpy.full(1000, 0.000)
for i in range(len(x)):
    y[i] += perlin1D(x[i])
    # print(str(i), " --> ", y[i])
print(x)
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()