from Model import Move, BeetleType


class AI:
    def __init__(self):
        self.heuristic_matrix = None
        self.team = 0
        self.price_dictionary = {
            "ally_normal": 1,
            "ally_wing": 2,
            "ally_sick": -0.5,
            "enemy_normal": -1,
            "enemy_wing": -0.5,
            "enemy_sick": -1,
            "food": 2,
            "trash": -2,
            "slipper": -5,
            "portal": 0
        }

    def do_turn(self, world):
        if world.get_current_turn() == 0:
            self.team = world.get_map().team
        self.initial_heuristic_matrix(world)
        self.update_heuristic_matrix(world)
        a = [0, 1, 2]
        print(world.get_map().get_game_2d_table())
        if world.get_current_turn() == 0:
            for i in range(0, 3):
                for j in range(0, 2):
                    for k in range(0, 3):
                        world.change_strategy(BeetleType.LOW.value, a[i], a[j], a[k], Move.step_forward)
                        world.change_strategy(BeetleType.HIGH.value, a[i], a[j], a[k], Move.step_forward)
        world.change_strategy(BeetleType.LOW.value, a[0], a[0], a[0], Move.step_forward)
        world.change_strategy(BeetleType.LOW.value, a[1], a[1], a[1], Move.turn_left)

    def initial_heuristic_matrix(self, world):
        self.heuristic_matrix = [[0] * world.get_map().get_height()] * world.get_map().get_width()

    def update_heuristic_matrix(self, world):
        for ally_beetle in world.get_my_beetles():
            self.propagate_ally_effect(ally_beetle)
        for enemy_beetle in world.get_opponent_beetles():
            self.propagate_enemy_effect(enemy_beetle)
        for food in world.get_foods_list():
            self.propagate_food_effect(food)
        for trash in world.get_trashes_list():
            self.propagate_trash_effect(trash)
        for slipper in world.get_slippers_list():
            self.propagate_slipper_effect(slipper)
        for teleport in world.get_teleport_list():
            self.propagate_teleport_effect(teleport)

    def propagate_ally_effect(self, ally_beetle):
        pass

    def propagate_enemy_effect(self, enemy_beetle):
        pass

    def propagate_food_effect(self, food):
        pass

    def propagate_trash_effect(self, trash):
        pass

    def propagate_slipper_effect(self, slipper):
        pass

    def propagate_teleport_effect(self, teleport):
        pass
