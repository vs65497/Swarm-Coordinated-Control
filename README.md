# Simulations from Coordinated Control of Multi-Robot Systems: A Survey
_Jorge Cortés &amp; Magnus Egerstedt_ - https://www.researchgate.net/publication/321863473_Coordinated_Control_of_Multi-Robot_Systems_A_Survey

Von Simmons, Fall 2022

# Background
Professor Egerstedt asked me to read "Coordinated Control of Multi-Robot Systems: A Survey" and simulate a few sections to gain a better understanding of its concepts. To my surprise, simulating the paper revealed some interesting points that I didn't expect. 

Just as context, swarms are collections of robots in which each "agent" runs on simple rules. Similar to a flock of birds or a school of fish, there is no overseer. Instead each agent just interacts with its neighbors. These local interactions then produce collective actions, known as emergent behaviors. At least this is the case in theory. I found that in order to control the swarm in a simulation I needed to make several assumptions.

# Goals
To simulate rendezvous, flocking, and cyclic pursuit behaviors.
- [**Rendezvous**](https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/README.md#rendezvous): All agents in the swarm converge to a single point in the center of the swarm. This is all without knowing where the entire swarm resides or the center of it lies.
- [**Flocking**](https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/README.md#flocking): All agents move in a collective direction. They come to consensus on the direction without external guidance.
- [**Cyclic Pursuit**](https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/README.md#cyclic-pursuit): Each agent moves towards its next neighbor (this requires an ordered cycle graph) with some offset angle.

# Assumptions
1. Onboard sensors can detect relative distance between agents.
2. Agents have access to bidirectional, peer-to-peer communication.
3. Detection range is software limited because the range of wifi and bluetooth makes testing impractical.
4. Agents are modeled as unicycles -- they can turn and move without complicated dynamics.
5. Graphs, connecting agents, are established beforehand without consensus.

When executing the simulations I needed to exercise centralized, top-down control over the agents to apply these assumptions. In the case of a physical system, these assumptions would need to be implemented in hardware. Even still, some amount of centralized control for the system overhead and communications may be necessary for the sake of experimentation.

# Results

_Please note_: `x` is the position vector, `phi` is the heading vector, `R` is the R^2 rotation matrix, `N` is the number of agents, `L` is the Laplacian Graph (L = Degree Matrix - Adjacency Matrix) 

Laplacian Graph: https://en.wikipedia.org/wiki/Laplacian_matrix

## Rendezvous
**Equation**: `x_dot = (-L * x)`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/rendezvous.py

<img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/rendezvous.png" width=300 />

## Flocking
**Equation**: `phi_dot = (-L * phi)`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/flocking.py

<img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/Screenshot%202022-10-24%20224551.png" width=300 />

## Cyclic Pursuit
**Equation**: `x_dot = R(-phi)*(x[i+1] - x[i])`, `i = 1,...,N-1`
<br />**Code**: https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/pursuit.py

_Converge_: `phi > pi / N` | _Unity_: `phi = pi / N` | _Diverge_: `phi < pi / N`
--- | --- | ---
<img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_converge.png" width=300 /> | <img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_unity.png" width=300 /> | <img src="https://github.com/zanzivyr/Swarm-Coordinated-Control/blob/main/results/cyclic_diverge.png" width=300 />

# Conclusion

Aside from the assumptions made to execute these concepts as simulations I also found that mathematics for individual agents does not necessarily reflect the reality of implementation. Mathematics serves as a tool to describe these concepts, but they do not express the entire situation. This was especially true when implementing agents as the unicycle model. Some of my earlier attempts led to behaviors that seemed very close to correct but didn't quite reach the mark. Because of this I learned that attempting to reproduce concepts leads to a much deeper understanding than simply reading. A lesson I'll take forward.

