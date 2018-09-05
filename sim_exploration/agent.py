import pommerman
from pommerman.agents import BaseAgent
import numpy as np
import time
import random


# List of details:
#	- 11x11:

# BOARD STATE
PASSAGE_IDX = 0
STONE_WALL_IDX = 1
WOODEN_WALL_IDX = 2
BOMB_IDX = 3
FLAMES_IDX = 4
FOG_IDX = 5
PU_EXTRA_BOMB_IDX = 6
PU_INC_RNG_IDX = 7
PU_CAN_KICK = 8
BOMB_BLAST_STRENGTH_IDX = 9
BOMB_LIFE_IDX = 10
# AGENT INFORMATION
# AGENTDUMMY=9, AGENT0=10, AGENT1=11, AGENT2=12, AGENT3=13
TEAMMATE_POS_IDX = 11 
MYPOSITION_POS_IDX = 12
ENEMY_POS_IDX = 13
MAX_NUM_PLANES = 14

# POWERUPS
NUM_AMMO_IDX = 0
BLAST_STRENGTH_IDX = 1
CAN_KICK_IDX = 2
# RADIO MESSAGE [1-8] 0 means no message

def map_to_matrix(obs):
	board_state = np.zeros((MAX_NUM_PLANES, 11, 11))

	teammate_idx = obs['teammate']
	enemy_idx_0 = obs['enemies'][0].value
	enemy_idx_1 = obs['enemies'][1].value
	enemy_idx_2 = obs['enemies'][2].value
	# print("ENEMY IDX ", dir(enemy_idx_0), enemy_idx_1, enemy_idx_2)

	board = obs['board']
	for i in range(11):
		for j in range(11):
			for k in range(PU_CAN_KICK+1):
				if(board[i,j] == k):
					board_state[k,i,j] = 1
			if(board[i,j] == teammate_idx and teammate_idx != 9):
				board_state[TEAMMATE_POS_IDX,i,j] = 1
			elif(board[i,j] == enemy_idx_0):
				board_state[ENEMY_POS_IDX,i,j] = 1
			elif(board[i,j] == enemy_idx_1):
				board_state[ENEMY_POS_IDX,i,j] = 1
			elif(board[i,j] == enemy_idx_2 and enemy_idx_2 != 9):
				board_state[ENEMY_POS_IDX,i,j] = 1

	pos_x, pos_y = obs['position']
	board_state[MYPOSITION_POS_IDX, pos_x, pos_y] = 1

	board_state[BOMB_BLAST_STRENGTH_IDX,:,:] = obs['bomb_blast_strength']
	board_state[BOMB_LIFE_IDX,:,:] = obs['bomb_life']

	powerups = np.zeros(3)
	powerups[NUM_AMMO_IDX] = obs['ammo']
	powerups[BLAST_STRENGTH_IDX] = obs['blast_strength']
	powerups[CAN_KICK_IDX] = obs['can_kick']


	return board_state, powerups


def get_hash(obs):
	# print(obs['board'].data)
	return hash(obs['board'].tostring())


play_num = 0
class RandomAgent(BaseAgent):
	"""The Random Agent that returns random actions given an action_space."""
	def __init__(self, *args, **kwargs):
		super(RandomAgent, self).__init__(*args, **kwargs)
		self.state_timeline = []
		self.time_stamp = 0
		print()
		return

	def set_neural_network(self, neural_network):
		self.neural_network = neural_network
		return

	def store_info(self, state, powerups, action):
		state_info = {
		"state" : state, 
		"powerups" : powerups,
		"action" : action, 
		"time_stamp" : self.time_stamp
		}
		self.state_timeline.append(state_info)
		self.time_stamp += 1
		return

	def get_state_timline(self):
		return self.state_timeline

	def MCTS_runs(self):
		return

	def act(self, obs, action_space):
		# print(obs)
		# print(action_space)
		global play_num
		play_num = play_num+1
		# print("AGENT ",play_num)
		# time.sleep(5)


		board_state, powerups = map_to_matrix(obs)
		action = random.randint(0,5)# action_space.sample()
		# print(get_hash(obs))

		# print("OBS ", obs, action_space)
		# for i in range(MAX_NUM_PLANES):
		# 	print(board_state[i])
		# print(powerups)

		# Store the decisions for learning later
		self.store_info(board_state, powerups, action)

		return action
