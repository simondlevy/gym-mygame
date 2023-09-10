#!/usr/bin/env python3
'''
Python distutils setup file for gym-mygame module.

Adapted from http://gym.openai.com/docs/

Copyright (C) 2020 Simon D. Levy

MIT License
'''

import gymnasium as gym

env = gym.make('gym_mygame:MyGame-v0')

for i_episode in range(20):

    observation, _ = env.reset(seed=123)

    for t in range(100):

        env.render()

        action = env.action_space.sample()

        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()
