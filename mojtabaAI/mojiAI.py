from Model import Move, BeetleType


class AI:
    def __init__(self):
        self.heuristic_matrix = None
        self.game_matrix = None
        self.team = 0
        self.map_width = 0
        self.map_height = 0

        # todo: main price factor should be base on wold constants => world.get_constants()
        # todo: what about << sick wing >> beetles ??
        # todo: this values are not accurate :) this is just for test
        self.price_dictionary = {
            "ally": {
                "normal": 1,
                "wing": 2,
                "sick": -0.5
            },
            "enemy": {
                "normal": 1,
                "wing": -0.5,
                "sick": -1
            },
            "food": 2,
            "trash": -2,
            "slipper": -5,
            "teleport": 0
        }

    def do_turn(self, world):
        if world.get_current_turn() == 0:
            self.team = world.get_map().team
            self.map_height = world.get_map().get_height()
            self.map_width = world.get_map().get_width()
        self.initial_heuristic_matrix(world)
        self.update_heuristic_matrix()
        print(self.heuristic_matrix)

    def initial_heuristic_matrix(self, world):
        self.heuristic_matrix = [[0] * world.get_map().get_height()] * world.get_map().get_width()
        self.game_matrix = world.get_map().get_game_2d_table()

    def update_heuristic_matrix(self):
        for col in self.game_matrix:
            for obj in col:
                if obj:
                    self.propagate_effect(obj)

    def propagate_effect(self, obj):
        obj_pos = obj.get_position()
        min_col_distance = [min(abs(obj_pos.col-col), abs(self.map_width-abs(obj_pos.col-col)))
                            for col in range(self.map_width)]
        min_row_distance = [min(abs(obj_pos.row-row), abs(self.map_height-abs(obj_pos.row-row)))
                            for row in range(self.map_height)]

        for col in range(self.map_width):
            for row in range(self.map_height):
                self.heuristic_matrix[col][row] += (min_col_distance[col] + min_row_distance[row]) * self.get_obj_price(obj)

    def get_obj_price(self, obj):
        obj_name = obj.__class__.__name__
        if obj_name == "Beetle":
            if obj.team == self.team:
                if obj.is_sick():
                    return self.price_dictionary["ally"]["sick"]
                elif obj.has_wing():
                    return self.price_dictionary["ally"]["wing"]
                else:
                    return self.price_dictionary["ally"]["normal"]
            else:
                if obj.is_sick():
                    return self.price_dictionary["enemy"]["sick"]
                elif obj.has_wing():
                    return self.price_dictionary["enemy"]["wing"]
                else:
                    return self.price_dictionary["enemy"]["normal"]
        else:
            return self.price_dictionary[obj_name.lower()]
