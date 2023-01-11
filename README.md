# Simulations from Coordinated Control of Multi-Robot Systems: A Survey
_Jorge Cortés &amp; Magnus Egerstedt_ - https://www.researchgate.net/publication/321863473_Coordinated_Control_of_Multi-Robot_Systems_A_Survey

Von Simmons, Fall 2022

# Background
Professor Egerstedt asked me to read this paper and simulate a few sections to gain a better understanding of the concepts. To my surprise, simulating the paper revealed some interesting points that I didn't expect. Just as context, swarms are collections of robots in which each robot, or "agent", runs on simple rules. There is not an overseer, instead each agent interacts with its neighbors. These local interactions then produce collective actions, known as emergent behaviors.

At least this is the case in theory. I found that in order to control the swarm in a simulation I needed to make several assumptions -- some which run counter to the premis of swarm robotics.

# Goals
To simulate rendezvous, flocking, and cyclic pursuit behaviors.
- **Rendezvous**: All agents in the swarm converge to a single point in the center of the swarm. This is all without knowing where the entire swarm or the center of it lies.
- **Flocking**: All agents move in a collective direction. They come to consensus on the direction without external guidance.
- **Cyclic Pursuit**: Each agent moves towards its next neighbor (this requires an ordered cycle graph) with some offset angle.

# Assumptions
1. Onboard sensors can detect relative distance between agents.
2. Agents have access to bidirectional, peer-to-peer communication.
3. Detection range is software limited because the range of wifi and bluetooth makes testing impractical.
4. Agents move as particles. They can change velocity instantaneously if necessary.
5. Graphs are established beforehand without consensus.

# Results

_Please note_: `x` is the position vector, `phi` is the heading vector, `R` is the R^2 rotation matrix, `N` is the number of agents, `L` is the Laplacian Graph (L = Degree Matrix - Adjacency Matrix) 

## Rendezvous
**Equation**: `x_dot = (-L * x)`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/rendezvous.py
<br /><img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/rendezvous.png" width=300 />

## Flocking
**Equation**: `phi_dot = (-L * phi)`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/flocking.py
<br /><img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/Screenshot%202022-10-24%20224551.png" width=300 />

## Cyclic Pursuit
**Equation**: `x_dot = R(-phi)*(x[i+1] - x[i])`, `i = 1,...,N-1`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/pursuit.py

_Converge_: `phi > pi / N`
<br /><img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_converge.png" width=300 />

_Unity_: `phi = pi / N`
<br /><img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_unity.png" width=300 />

_Diverge_: `phi < pi / N`
<br /><img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_diverge.png" width=300 />

