import numpy as np
from numpy import linalg as LA
import random
from tkinter import *
import math

# INITIALIZATION

count = 5
xmax = 500
ymax = 500
maxrange = xmax*0.3
maxsteps = 60
v = 3 # pixels (distance)
offset = -110 * 3.1415 / 180
dt = 0.02 # seconds

agents = np.array([])
#print(agents)

for i in range(count):
  id = "agent-" + str(i)
  x = random.randint(xmax*.2, xmax*.8)
  y = random.randint(ymax*.2, ymax*.8)
  phi = random.randint(0,360) * 3.1415 / 180

  agt = np.array([id, np.array([x, y, phi]), np.zeros((count))])
  agents = np.append(agents, agt, axis=0)

agents = np.reshape(agents, (count,3))

for i in range(count):
  for j in range(count):
    dist = LA.norm(agents[i][1] - agents[j][1])
    agents[i][2][j] = dist

#agents

# LAPLACIAN GRAPH

n = agents[0][2].size
deg = np.zeros((n,n))
adj = np.zeros((n,n))

for i in range(n):
    degree = 0
    for e in range(n):
        if(agents[i][2][e] <= maxrange):
            adj[i][e] = 1
            adj[e][i] = 1
            adj[i][i] = 0
            degree += 1

    deg[i][i] = degree

lapl = deg - adj
#print(deg)
#print(adj)
#print(lapl)

# CREATE X

pos = np.array([])

for p in range(n):
  pos = np.append(pos, agents[p][1])

pos = np.reshape(pos, (n,3))

# CONSENSUS EQUATION

root = Tk()
root.title('Swarm - Flocking')
root.geometry(str(xmax+50)+"x"+str(ymax+50))
my_canvas = Canvas(root, width=xmax+xmax*.2, height=ymax+ymax*.2, bg="white")
my_canvas.pack(pady=20)

def draw(pos, pad):
    # Draw agents
    color = ["red", "blue", "green", "yellow", "purple"]
    for i in range(n):
        center = pos[i]
        cx = center[0]+5
        cy = center[1]+5
        my_canvas.create_rectangle(cx-pad, cy-pad, cx+pad, cy+pad, fill=color[i])

draw(pos, 1)

for step in range(maxsteps):
    # MOVE
    # (Mix in the timestep)
    # xdot / dt = -L * x
    # xdot = (-L * x) * dt
    # deltaphi = (-L * phi) * dt
    phidot = -1 * lapl@pos[:,2]
    deltaphi = phidot * dt

    # This is updated heading
    pos[:,2] += deltaphi
    
    # Update x,y position. AKA move here!
    
    # bounds should be [0, 180] and [0, -180]
    for j in range(n):
      if pos[j,2] > 3.1415:
        # 190 -> -360 + 190 = -170
        pos[j,2] = -(2*3.1415)+pos[j,2]

    #pos[:,0] += np.sign(np.cos(pos[:,2])) * v*np.cos(pos[:,2])
    pos[:,0] += v*np.cos(pos[:,2])
    pos[:,1] += v*np.sin(pos[:,2])

    print("direction")
    print(pos[:,2])
    print(v*np.cos(pos[:,2]))

    pad = 2
    if step == maxsteps-1: pad = 5
    draw(pos, pad)

# execute window
root.mainloop()