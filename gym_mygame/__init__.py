from gymnasium.envs.registration import register

register(
    id='MyGame-v0',
    entry_point='gym_mygame.envs:MyGame',
    max_episode_steps=10000
)
