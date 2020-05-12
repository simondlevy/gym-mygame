#!/usr/bin/env python3
'''
Python distutils setup file for gym-mygame module.

Adapted from http://gym.openai.com/docs/

Copyright (C) 2020 Simon D. Levy

MIT License
'''

import gym

env = gym.make('gym_mygame:MyGame-v0')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()
