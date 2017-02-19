from random import randint

from Model import Move, BeetleType

__author__ = 'RezaS'


class AI:
    def do_turn(self, world):
        print(world.get_current_turn())

        a = [0, 1, 2]

        if world.get_current_turn() == 0:
            for i in range(0,3):
                for j in range(0,2):
                    for k in range(0,3):
                        world.change_strategy(BeetleType.LOW.value, a[i], a[j], a[k], Move.step_forward)
                        world.change_strategy(BeetleType.HIGH.value, a[i], a[j], a[k], Move.step_forward)