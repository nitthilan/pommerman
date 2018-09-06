import pommerman
from pommerman import agents
import numpy as np
import argparse
from copy import deepcopy


# Data collected using featurize function
train_filepath = "../../../../data/multiagent_rl/simple_600K_disc0.99_cleaned.npz"
valid_filepath = "../../../../data/multiagent_rl/valid_100K_disc0.99_cleaned.npz"

def featurize(obs):
    # TODO: history of n moves?
    board = obs['board']

    # convert board items into bitmaps
    maps = [board == i for i in range(10)]
    maps.append(obs['bomb_blast_strength'])
    maps.append(obs['bomb_life'])

    # duplicate ammo, blast_strength and can_kick over entire map
    maps.append(np.full(board.shape, obs['ammo']))
    maps.append(np.full(board.shape, obs['blast_strength']))
    maps.append(np.full(board.shape, obs['can_kick']))

    # add my position as bitmap
    position = np.zeros(board.shape)
    position[obs['position']] = 1
    maps.append(position)

    # add teammate
    if obs['teammate'] is not None:
        maps.append(board == obs['teammate'].value)
    else:
        maps.append(np.zeros(board.shape))

    # add enemies
    enemies = [board == e.value for e in obs['enemies']]
    maps.append(np.any(enemies, axis=0))

    return np.stack(maps, axis=2)


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
# for i in range(18):
# 	print(observations[10,:,:,i])

