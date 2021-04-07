import arcade
from entities import *
from mapgen import *
from camera import *
from constants import *

class Game(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.map = Map()
        self.map.useRoomAddition()
        self.map.renderTiles()

        # Set up the player, then spawning it at random location on the map
        self.player_sprite = Player(0, 0,":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.15)
        self.player_sprite.spawn_player(self.map.tilesbg_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.map.tiles_list)

        #Camera object
        self.camera = Camera(CAMERA_WIDTH, CAMERA_HEIGHT, self.player_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        #Draw map
        self.map.tiles_list.draw()
        self.map.tilesbg_list.draw()

        # Draw our sprites
        EntityManager.draw_entities()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        EntityManager.handle_key_press(key)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        EntityManager.handle_key_release(key)

    def on_update(self, delta_time):
        """ Movement and game logic """
        #Physics engine
        self.physics_engine.update()

        #Entity updates
        EntityManager.move_entities()
        EntityManager.update_entities(delta_time)

        #Camera update
        self.camera.camera_update()

def main():
    """ Main method """
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()