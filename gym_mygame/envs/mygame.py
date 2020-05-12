'''
My OpenAI Gym game environment for CSCI 316 spring 2020

Copyright (C) 2020 A. Student

MIT License
'''

import gym

import numpy as np

class MyGame(gym.Env):

    def __init__(self):

        gym.Env.__init__(self)

        # Use [-1,+1] for observation space an action space
        self.observation_space = gym.spaces.Box(-1, +1, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Box(-1, +1, (1,), dtype=np.float32)

        self.reset()

    def step(self, action):

        state = [0]
        reward = 0
        done = False
        info = {}

        return state, reward, done, info

    def render(self, mode='human'):

        return

    def reset(self):

        return [0]

    def close(self):

        gym.Env.close(self)

        
