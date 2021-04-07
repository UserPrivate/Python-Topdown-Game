import arcade
import entities

#WIP
class EntityManager:
    entities = []
    player_list = arcade.SpriteList()

    @classmethod
    def add_entity(cls, entity):
        cls.entities.append(entity)
        if isinstance(entity, entities.Player):
            cls.player_list.append(entity)

    @classmethod
    def draw_entities(cls):
        cls.player_list.draw()

    @classmethod
    def handle_key_press(cls, key):
        for e in cls.entities:
            e.input_press(key)

    @classmethod
    def handle_key_release(cls, key):
        for e in cls.entities:
            e.input_release(key)

    @classmethod
    def move_entities(cls):
        for e in cls.entities:
            e.move()

    @classmethod
    def update_entities(cls, delta_time):
        for e in cls.entities:
            e.update(delta_time)
