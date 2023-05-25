import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import OBSTACLE_Y_POS

class Bird(Obstacle):
    def __init__(self, images):
        super().__init__(images[0]) #iniciando com uma imagem inicial
        varia_y = random.randint(-90,20)
  
        self.ini_y_pos = 380 + varia_y
        self.images = images #array de images
        self.rect.y = self.ini_y_pos #desenhando no ar
        self.flying_index = 0 #usado para mudar a imagen
                  
    def update(self, game_speed, obstacles):
        self.fly()
        
        if self.flying_index > 9:
            self.flying_index = 0
        
        super().update(game_speed, obstacles)
        
    def fly(self):
        self.image = self.images[self.flying_index//5]
        self.flying_index += 1
        