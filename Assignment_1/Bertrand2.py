import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def randompointoncircle(radius,center):
    theta = random.random() * 2 * math.pi
    x = center[0] + radius * math.cos(theta)
    y = center[1] + radius * math.sin(theta)
    return (x, y)

def anglewithx(point):
    return point[1]/(point[0]+1)

# Make a circle with center at (0,0) and radius 1
fig, ax = plt.subplots()
circle = Circle((0,0),1,fill=False)
ax.add_artist(circle)
ax.set_xlim((-1,1))
ax.set_ylim((-1,1)) 
ax.set_aspect('equal', adjustable='box')

# Make an equilateral triangle with side length 1 and vertices at (-1,0) (1/2, sqrt(3)/2) and (1/2, -sqrt(3)/2)
triangle = plt.Polygon([(-1,0),(1/2,math.sqrt(3)/2),(1/2,-math.sqrt(3)/2)],fill=False)
ax.add_patch(triangle)

count = 0
for i in range(200):
    x, y = randompointoncircle(1, (0,0))
    plt.scatter(x, y, color='blue', s=5)  # smaller scatter plot dots

    if anglewithx([x,y]) <= 1/math.sqrt(3) and anglewithx([x,y]) >= -1/math.sqrt(3):
        mycolor = (0, 0.5, 0, 0.5)  # Slightly darker green lines
    else:
        mycolor = (0.5, 0, 0, 0.5)  # Slightly darker red lines
    plt.plot([-1, x], [0, y], color=mycolor, linewidth=0.5)  # Adjusted line thickness

for i in range(10000):
    x, y = randompointoncircle(1, (0,0))
    if anglewithx([x,y]) <= 1/math.sqrt(3) and anglewithx([x,y]) >= -1/math.sqrt(3):
        count += 1
print("Number of points inside triangle is ", count/10000)

plt.show()
