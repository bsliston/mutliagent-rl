import abc
from collections import namedtuple
from typing import Dict, Optional

import pdb


class AgentTrainer:
    def __init__(self, agents, env, replay):
        self._agents = agents
        self._env = env
        self._replay = replay

        self._replay_keys = [
            "state_t",
            "action_t",
            "reward_t",
            "state_tp1",
            "action_tp1",
            "done_t",
        ]

    @property
    def replay_keys(self):
        return self._replay_keys

    def train_episode(self):
        self.run_episode()

    def run_episode(self):
        self._env.reset()
        memory = namedtuple("Memory", self.replay_keys)

        for agent in self._env.agent_iter():
            print(agent)
            state_t, reward_t, done_t, info_t = self._env.last()
            if done_t:
                break
            self._env.step(self._env.action_space(agent).sample())

            pdb.set_trace()

        pdb.set_trace()

    def _train_samples(self):
        return NotImplemented

    def _add_to_replay(self):
        return NotImplemented


if __name__ == "__main__":
    pass
