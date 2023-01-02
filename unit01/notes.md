Deep Reinforcement Learning


Exploración vs. Explotación
* Exploration is exploring the environment with random actions in order to find out more things about the environment itself.
* Exploitation is exploring known information to maximize the reward.

The main goal of the RL Agent is to maximize the expected cumulative reward.


The policy π

This policy is the brain of our agent, is the function that tells us what action to take given the state we are. So it defines the agent behavior at a given time.

So at the end, we want to learn the optimal policy π that maximizes the expected returned reward. As this is DRL, we are doing this by a training process.


There are two approaches:
* Directly, by teaching the agent which action to take given the current state: The called Policy-Based Methods.
    * We learn a policy function. It will define a probability distribution over the set of possible actions at that state. That means that the policy is deterministic (given a states it will return the same action).
    * The policy function can be also Stochastic. That means that the output is a probability distribution over the actions.
* Indirectly, teach the agent to learn which state is more valuable and then take the action that leads to the more valuable states: Value-Based Methods.
    * Here instead of training a policy function, we train a value function that maps a state to the expected value of being at that state.
    * The value of the state is the expected discounted return the agent can get if it starts in that state, and then act according to our policy (the policy is basically the highest value).
