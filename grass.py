from pico2d import load_image

import game_world


class Grass:
    def __init__(self, y):
        self.image = load_image('grass.png')
        self.y = y

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
