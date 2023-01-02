import gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

env = gym.make('LunarLander-v2')
model = PPO('MlpPolicy', env, verbose=1)

model.learn(total_timesteps=1000000)

model_name = "drl-lunarLander-v2"
model.save(model_name)

# Create the environment
# env = make_vec_env('LunarLander-v2', n_envs=16)

# Load the trained agent
# NOTE: if you have loading issue, you can pass `print_system_info=True`
# to compare the system on which the model was trained vs the current one
# model = DQN.load(model_name, env=env, print_system_info=True)
eval_env = gym.make('LunarLander-v2')

# Evaluate the model with 10 evaluation episodes and deterministic=True 
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)


print("Mean reward: ", mean_reward)
print("STD reward: ", std_reward)