import random
from Animals.Animal import Animal


class Sheep(Animal):
    def __init__(self, world, X=None, Y=None, generation=None):
        super().__init__()
        if X is None and Y is None and generation is None:
            while True:
                x = random.randint(1, world.GetWidth())
                y = random.randint(1, world.GetHeight())
                if world.GetElement(x, y) == ' ':
                    self.X = x
                    self.Y = y
                    break
            self.generation = 1
        else:
            self.X = X
            self.Y = Y
            self.generation = generation
        self.initiative = 4
        self.power = 4
        self.world = world
        self.identity = 'S'
        self.name = "Sheep"
        self.alive = True
        self.color = "PaleGreen2"

    def NewBorn(self, x, y):
        return Sheep(self.world, x, y, self.generation + 1)
