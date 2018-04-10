import gym
import random
import numpy as np 
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

LR = 1e-3
env = gym.make('CartPole-v0')
env.reset()
goal_steps = 500
score_requirement = 50
initial_games = 1e4


def some_radom_games_first():
	for episode in range(1000):
		#env.reset()
		for t in range(goal_steps):
			env.render()
			action = env.action_space.sample()
			observationsm, reward, done, info =env.step(action)
			if done:
				break

some_radom_games_first()


