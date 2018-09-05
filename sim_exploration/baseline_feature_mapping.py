import pommerman
from pommerman import agents
import numpy as np
import argparse
from copy import deepcopy



train_filepath = "../../../data/multiagent_rl/simple_600K_disc0.99_cleaned.npz"
valid_filepath = "../../../data/multiagent_rl/valid_100K_disc0.99_cleaned.npz"


def get_pommerman_data(filepath):
	npz_data = np.load(filepath)
	print(npz_data.keys())
	observations = npz_data['observations']
	actions = npz_data['actions']
	rewards = npz_data['rewards']
	# values = npz_data['values']
	return (observations, actions, rewards)

(observations, actions, rewards) = \
 	get_pommerman_data(valid_filepath)

print(rewards.shape, observations.shape)
for i in range(18):
	print(observations[10,:,:,i])
