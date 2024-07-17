import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def randompointincircle(radius):
    r = radius * math.sqrt(random.random())
    theta = random.random() * 2 * math.pi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def pointisincircle(x, y, radius):
    return x**2 + y**2 < radius**2
    
def getendpoints(radius,x,y):
    m= -x/y
    c = y + x**2/y
    A = m**2 + 1
    B = 2*m*c
    C = c**2 - radius**2
    d = (B**2 - 4*A*C)**0.5
    x1 = (-B + d)/(2*A)
    x2 = (-B - d)/(2*A)
    y1 = m*x1 + c
    y2 = m*x2 + c
    return (x1,y1),(x2,y2)


def main():
    radius = 1
    n = 200

    # Make a circle
    fig, ax = plt.subplots()
    circle = Circle((0,0),radius,fill=False)
    ax.add_artist(circle)
    ax.set_xlim((-radius,radius))
    ax.set_ylim((-radius,radius))
    ax.axis('on')
    # Set the aspect ratio to be equal
    ax.set_aspect('equal', adjustable='box')
    # Show the grid and coordinates of the circle
    ax.grid(True)
    circle = Circle((0,0),radius/2,fill=False,color='grey',linestyle='dotted')
    ax.add_patch(circle)

    for i in range(n):
        x, y = randompointincircle(radius)
        if pointisincircle(x, y, 1/2):
            # Add the chord in green color
            endpoints = getendpoints(radius,x,y)
            plt.plot([endpoints[0][0],endpoints[1][0]],[endpoints[0][1],endpoints[1][1]],color=(0,0.5,0,0.2), linewidth=0.5)  # slightly darker green lines
            plt.scatter(x,y,color='blue', s=5, alpha=0.5)  # smaller points
        else:
            # Add the chord in red color
            endpoints = getendpoints(radius,x,y)
            plt.plot([endpoints[0][0],endpoints[1][0]],[endpoints[0][1],endpoints[1][1]],color=(0.5,0,0,0.2), linewidth=0.5)  # slightly darker red lines
            plt.scatter(x,y,color='grey', s=5, alpha=0.5)  # smaller points

    # Count the number of chords that are greater than the side of an equilateral triangle
    n=100000
    count=0
    for i in range(n):
        x, y = randompointincircle(radius)
        if pointisincircle(x, y, 1/2):
            count += 1       
    print("The ratio of chords greater than the side of an equilateral triangle:", count/n)
    plt.show()

main()
