import pommerman
from pommerman import agents
import agent as sa
from multiprocessing import Pool


# file:///Users/kannappanjayakodinitthilan/Documents/myfolder/project_devan/aws_workspace/source/generators/renderer/alpha_go_zero_cheat_sheet.png
# parameters
# Number of self-play gamees for training

def run_one_episode(arguments):
    neural_network, environment, num_episodes, instance_id \
        = arguments

    # Create a Agent list using the neural network
    agent_list = [
        sa.RandomAgent(),
        sa.RandomAgent(),
        sa.RandomAgent(),
        sa.RandomAgent()
    ]

    env = pommerman.make(environment, agent_list)

    # Run the episodes just like OpenAI Gym
    for i_episode in range(int(num_episodes)):
        state = env.reset()
        done = False
        while not done:
            # env.render()
            actions = env.act(state)
            state, reward, done, info = env.step(actions)

        print('Episode {} finished'.format(i_episode))
    env.close()

    return

def training_set_generation_loop(neural_network):
    # ['PommeFFACompetition-v0', 'PommeFFACompetitionFast-v0', 
    #  'PommeFFAFast-v0', 'PommeFFA-v1', 'PommeRadio-v2', 
    #  'PommeTeamCompetition-v0', 'PommeTeam-v0', 'PommeTeamFast-v0']
    environment = 'PommeFFACompetition-v0' #'PommeTeamCompetition-v0'
    NUM_TRAINING_GAMES = 5
    pool_size = 4

    # Generate inputs for pool_size
    arguments = []
    num_episodes = NUM_TRAINING_GAMES/pool_size
    neural_network = "dummy_name"
    for i in range(pool_size):
        arguments.append((neural_network, environment, num_episodes, i))


    # Map it to multiple process
    process_pool = Pool()
    results = process_pool.map(run_one_episode, arguments)

    print([result for result in results])
    return

def training_neural_network():
    return

def evaluate_new_network():
    return

def outer_loop():
    # Initialize the agents

    # Choose the competition
    # Start with single, then double agent, then foggy environment


    # Run some 100 episodes with the 

    # Each episode store the game state, MCTS roll out probabilities and winner

    # Retrain the neural network, from the last 500000 games

    # Evaluate the new trained agent

    return

def main():
    # Print all possible environments in the Pommerman registry
    print(pommerman.registry)

    # Create a set of agents (exactly four)
    agent_list = [
        # agents.SimpleAgent(),
        # agents.SimpleAgent(),
        # agents.SimpleAgent(),
        # agents.SimpleAgent(),
        sa.RandomAgent(),
        sa.RandomAgent(),
        sa.RandomAgent(),
        sa.RandomAgent()
        # agents.DockerAgent("pommerman/simple-agent", port=12345),
    ]
    # Make the "Free-For-All" environment using the agent list
    # ['PommeFFACompetition-v0', 'PommeFFACompetitionFast-v0', 'PommeFFAFast-v0', 'PommeFFA-v1', 'PommeRadio-v2', 'PommeTeamCompetition-v0', 'PommeTeam-v0', 'PommeTeamFast-v0']
    # env = pommerman.make('PommeFFACompetitionFast-v0', agent_list)
    env = pommerman.make('PommeFFACompetition-v0', agent_list)
    # env = pommerman.make('PommeTeamCompetition-v0', agent_list)

    # Run the episodes just like OpenAI Gym
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            # env.render()
            actions = env.act(state)
            print("Actions every step ", actions)
            state, reward, done, info = env.step(actions)
            print("One step ")
            # print("State ", state) # Array of 4 states
            print("Reward ", reward)  # -1, 0 ,1
            # print("Done ", done) # False/True
            # print("Info ", info) # {'result': <Result.Win: 0>, 'winners': [3]}
        print('Episode {} finished'.format(i_episode))

        # for i, al in enumerate(agent_list):
        #     print("Agent Idx ", i, al.get_state_timline())
    env.close()


if __name__ == '__main__':
    # main()
    training_set_generation_loop("dummy")
