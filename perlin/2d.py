import numpy
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

def fade(t): 
    return t ** 3 * (t * (t * 6 - 15) + 10)
 
def lerp(t, a, b):
    return a + t * (b - a)

def grad2D(hash, x, y):
    h = hash & 15
    u = x if h < 4 or h in (12, 15) else -x
    v = y if h < 8 else -y
    return u+v

permutation = [151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

p = [None] * 512
for i in range(256):
    p[256+i] = p[i] = permutation[i]

def perlin2D(x,y):
    x, y = x%255, y%255
    low_x, low_y = math.floor(x), math.floor(y)
    dist_x, dist_y = x-low_x, y-low_y
    A = int(p[int(x)  ] + y)
    B = int(p[int(x+1)] + y)
    return lerp(dist_y, lerp(dist_x, fade(grad2D(p[A]  , x  , y  )), fade(grad2D(p[B]  , x+1, y  ))),
                        lerp(dist_x, fade(grad2D(p[A+1], x+1, y+1)), fade(grad2D(p[B+1], x  , y+1))) )

x = numpy.linspace(0, 255, 500)
y = numpy.linspace(0 ,255 ,500)
Z = numpy.full((500,500), 0.00)
for i in range(500):
    for j in range(500):
        Z[i,j] = perlin2D(x[i], y[j])
X, Y = numpy.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

another_fig = plt.figure()
another_ax = plt.axes(projection='3d')
another_ax.plot_surface(X, Y, Z, edgecolor='none')
another_ax.set_xlabel('x')
another_ax.set_ylabel('y')
another_ax.set_zlabel('z')

plt.show()