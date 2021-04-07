import arcade
import random
from entitymanager import EntityManager
from statemachine import FSM
from constants import *

class Entity(arcade.Sprite):
    def __init__(self, x, y, img, scale):
        super().__init__(img, scale)
        EntityManager.add_entity(self)
        self.center_x = x
        self.center_y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.dt = 0


    def input_press(self, key) -> None:
        pass

    def input_release(self, key) -> None:
        pass

    def move(self) -> None:
        pass

    def update(self, delta_time) -> None:
        pass

class Player(Entity):
    def __init__(self, x, y, img, scale):
        super().__init__(x, y, img, scale)
        self.FSM = FSM()
        self.placed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def spawn_player(self, wall_list):
        while not self.placed:
            
            # Randomly position
            max_x = SCREEN_WIDTH
            max_y = SCREEN_HEIGHT

            self.center_x = random.randrange(max_x)
            self.center_y = random.randrange(max_y)

            walls_hit = arcade.check_for_collision_with_list(self, wall_list)
            if len(walls_hit) == 1:
                self.placed = True

    def input_press(self, key) -> None:
        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def input_release(self, key) -> None:
        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    #FSM WIP IMPLEMENTATION        
    def idle(self):
        pass

    def run(self):
        pass

    def jump(self):
        pass

    def move(self):
        self.velocity_y = 0
        self.velocity_x = 0

        if self.up_pressed and not self.down_pressed:
            self.velocity_y = MOVEMENT_SPEED * self.dt
        elif self.down_pressed and not self.up_pressed:
            self.velocity_y = -MOVEMENT_SPEED * self.dt
        if self.left_pressed and not self.right_pressed:
            self.velocity_x = -MOVEMENT_SPEED * self.dt
        elif self.right_pressed and not self.left_pressed:
            self.velocity_x = MOVEMENT_SPEED * self.dt

    def update(self, delta_time) -> None:
        self.dt = delta_time
        self.center_x += self.velocity_x
        self.center_y += self.velocity_y
