import numpy as np
from numpy import linalg as LA
import random
from tkinter import *

# INITIALIZATION

count = 5
xmax = 500
ymax = 500
maxrange = xmax
maxsteps = 10

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

# LAPLACIAN GRAPH

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
print(adj)
#print(lapl)

# CREATE X

pos = np.array([])

for p in range(n):
  pos = np.append(pos, agents[p][1])

pos = np.reshape(pos, (n,2))
#pos

# CONSENSUS EQUATION

root = Tk()
root.title('Swarm - Rendezvous')
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
    #xdot = np.dot(-1 * lapl, pos)

    sum = np.zeros((n,2))
    for i in range(n):
      for j in range(n):
        if adj[i][j] == 1:
          sum[i] += (agents[i][1] - agents[j][1])
          #print(sum)
          #print(adj[i][j])

    xdot = -1 * sum

    # MOVE
    # (Mix in the timestep)
    # xdot / dt = -L * x
    # xdot = (-L * x) * dt

    dt = 0.02 # seconds
    deltax = xdot * dt
    #xpos

    # This is updated position. AKA move here!
    pos += deltax
    #pos

    pad = 2
    if step == maxsteps-1: pad = 5
    draw(pos, pad)

# execute window
root.mainloop()