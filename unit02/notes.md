
## Q-Learning


Finding an optimal *value function (Q* or V*)* leads to having an optimal policy.


- In state-value function, we calculate the value of a state St

- In action-value function, we calculate the value of the state-action pair (St, At) hence the value of taking that action a that state.

The problem is that it implies that to calculate EACH value of a state or a state-action pair, we need to sum all the rewards an agent can get if it starts at that state.

This can be a computationally expensive process, and that’s where the Bellman equation comes to help us.


The Bellman equation simplifies our state value or state action value calculation.

If we calculate V(St) (value of a state), we need to calculate the return start at that state and then follow the policy forever after



### Monte Carlo: Learning at the end of the episode

Monte Carlo is a strategy on how to train our value function or our policy function. It uses experience to solve the RL problem.

Montecarlo uses an entire episode of experience before learning.