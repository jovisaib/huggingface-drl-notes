
## Q-Learning

**Epsilon Greedy Strategy:** A policy that alternates between exploration (random action) and exploitation.

**The value of a state, or a state-action pair is the expected cumulative reward our agent gets if it starts at this state (or state-action pair) and then acts accordingly to its policy.**

**The reward is the feedback I get from the environment after performing an action at a state.**


**Off-policy: using a different policy for acting (inference) and updating (training).**


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


### Monte Carlo and RD

To summarize the policy learning methods:

-  With Monte Carlo, we update the value function from a complete episode (e.g. cat eats the mouse or if the mouse moves > 10 steps), and so we use the actual accurate discounted return of this episode.

- With TD Learning, we update the value function from a step, so we replace Gt that we don't have with an estimated return called TD target.