from random import randint

from Model import Move, BeetleType

__author__ = 'RezaS'


class AI:
    def __init__(self):
        super().__init__()
        self.hoosh_ro_id = 0

    def do_turn(self, world):
        print("turn: ",world.get_current_turn())
        index = 0
        for slipp in world.get_map().get_slippers_list():
            index += 1;
            print("slipp",index," :",dir(slipp))

        if world.get_current_turn() == 0:
            self.first_turn(world=world)
        else:
            self.update_strategy_randomly(world=world)

    # update each action with 50 percentage probability , and choose action uniform randomly
    def update_strategy_randomly(self, world):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 2):
                    rand_number = randint(0, 100)
                    if rand_number > 50:
                        which_action = randint(0, 300) % 3
                        if which_action ==0:
                            world.change_strategy(beetle_type=BeetleType.LOW.value, front_left=i, front=k, front_right=j
                                                  , move_strategy=Move.turn_right)
                        elif which_action ==1:
                            world.change_strategy(beetle_type=BeetleType.LOW.value, front_left=i, front=k, front_right=j
                                                  , move_strategy=Move.step_forward)
                        else:
                            world.change_strategy(beetle_type=BeetleType.LOW.value, front_left=i, front=k, front_right=j
                                                  , move_strategy=Move.turn_left)
                    rand_number = randint(0, 100)
                    if rand_number > 50:
                        which_action = randint(0, 300) % 3
                        if which_action == 0:
                            world.change_strategy(beetle_type=BeetleType.HIGH.value, front_left=i, front=k
                                                  , front_right=j, move_strategy=Move.turn_right)
                        elif which_action == 1:
                            world.change_strategy(beetle_type=BeetleType.HIGH.value, front_left=i, front=k
                                                  , front_right=j, move_strategy=Move.step_forward)
                        else:
                            world.change_strategy(beetle_type=BeetleType.HIGH.value, front_left=i, front=k
                                                  , front_right=j, move_strategy=Move.turn_left)

    def first_turn(self, world):

        self.hoosh_ro_id = world.get_team_id()
        print("team id: ",self.hoosh_ro_id)
        # beetles = world.get_map().get_beetles_list()
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 2):
                    world.change_strategy(beetle_type=BeetleType.LOW.value, front_left=i, front=k, front_right=j
                                          , move_strategy=Move.step_forward)
                    world.change_strategy(beetle_type=BeetleType.HIGH.value, front_left=i, front=k, front_right=j
                                          , move_strategy=Move.step_forward)