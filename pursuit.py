import numpy as np
from numpy import linalg as LA
import random
from tkinter import *
import math

# INITIALIZATION

count = 3
xmax = 500
ymax = 500
maxrange = xmax*0.3
maxsteps = 300

agents = np.array([])
#print(agents)

for i in range(count):
  id = "agent-" + str(i)
  x = random.randint(xmax*.2, xmax*.8)
  y = random.randint(ymax*.2, ymax*.8)

  agt = np.array([id, np.array([x, y]), np.zeros((count))])
  agents = np.append(agents, agt, axis=0)

agents = np.reshape(agents, (count,3))

for i in range(count):
  for j in range(count):
    dist = LA.norm(agents[i][1] - agents[j][1])
    agents[i][2][j] = dist

#agents
n = agents[0][2].size

# CREATE X

pos = np.array([])

for p in range(n):
  pos = np.append(pos, agents[p][1])

pos = np.reshape(pos, (n,2))
#pos

# CONSENSUS EQUATION

root = Tk()
root.title('Swarm - Circular Pursuit')
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

# rotation matrix
# R(2,2)
phi = 1.0 * math.pi / n   # unity
phi = 0.7 * math.pi / n   # converge
phi = 1.3 * math.pi / n   # diverge
#phi = 0
#phi = -1.56
rot = np.zeros((n,n))
rsmall = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])

for step in range(maxsteps):

    # cycle graph, x[i+1] - x[i]
    error = np.zeros((n,2))
    for e in range(n):
      if e+1 == n:
        error[e] = pos[0] - pos[e]
      else:
        error[e] = pos[e+1] - pos[e] 

    # ROTATE
    # xdot = R(-phi)*error
    xdot = np.zeros((n,2))
    for i in range(n):
      xdot[i] = np.dot(rsmall, error[i])
      xdot[i] /= LA.norm(xdot[i])

    v = 10 # pixels
    dt = .2 # seconds
    deltax = v * xdot * dt

    # This is updated position. AKA move here!
    pos += deltax

    pad = 2
    if step == maxsteps-1: pad = 5
    draw(pos, pad)

# execute window
root.mainloop()