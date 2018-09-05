# Pommerman

## Folder Structure
- data_gen : Code related to data generation for training
- training : Code related to train the neural network
- docker : Docker for running neural networks
- web_app : for human interaction

## To Do List


## State
- 11x11 board:
	- hardwall, box, passage, player, partner, enemy, bomb, flames
	- fog
	- bomblife, bomb strength
- 

## Questions:
- How is partial information encoded?
- How is Power-Ups encoded? Bomb, Range, Can-Kick
- How many past information should I store?

## Data Augumentation:
- flip the board across all the dimensions
- simulate the partial visibility??
- switch the agents, enimies
- Simulate the end cases by randomly generation of all possible end conditions?


## References:
- https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-i-q-learning-sarsa-dqn-ddpg-72a5e0cb6287
- https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-part-ii-trpo-ppo-87f2c5919bb9
- TRPO: https://arxiv.org/pdf/1502.05477.pdf
- PPOA: https://arxiv.org/pdf/1707.06347.pdf

## Other
- https://help.github.com/articles/basic-writing-and-formatting-syntax/