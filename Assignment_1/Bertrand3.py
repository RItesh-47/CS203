import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def randomdistance(r):
    return random.random() * r

def getendpoints(r,x,y):
    if (y==0):
        return (x,(r**2-x**2)**0.5),(x,-(r**2-x**2)**0.5)
    m= -x/y
    c = y + x**2/y
    A = m**2 + 1
    B = 2*m*c
    C = c**2 - r**2
    d = (B**2 - 4*A*C)**0.5
    x1 = (-B + d)/(2*A)
    x2 = (-B - d)/(2*A)
    y1 = m*x1 + c
    y2 = m*x2 + c
    return (x1,y1),(x2,y2)

count=0
r=1  #radius

fig, ax = plt.subplots()
circle = Circle((0,0),r,fill=False)
ax.add_artist(circle)
ax.set_xlim((-r,r))
ax.set_ylim((-r,r))
ax.axis('on')
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

for i in range(200):
    x = randomdistance(r)
    endpoints = getendpoints(r,x,0)  
    if x <= 1/2:
        mycolor=(0,1,0,0.5)   
    else:
        mycolor=(1,0,0,0.5)  
    plt.plot([endpoints[0][0],endpoints[1][0]],[endpoints[0][1],endpoints[1][1]], color=mycolor, linewidth=0.5)  # Adjusted line thickness
    plt.scatter(x, 0, color='black', s=5)  # Smaller scatter plot dots

plt.show()

count=0
for i in range(100000):
    x = randomdistance(r)
    if x <= 1/2:
        count += 1
print("The required probability is:", count/100000)
