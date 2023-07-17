import random
from Animals.Animal import Animal


class Fox(Animal):
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
        self.initiative = 7
        self.power = 3
        self.world = world
        self.identity = 'F'
        self.name = "Fox"
        self.alive = True
        self.color = "orange"

    def Action(self):
        super().Action()
        org = self.world.GetOrganism(self, self.X, self.Y)
        if org is None:
            return
        if org.GetPower() > self.power:
            self.X = self.prev_X
            self.Y = self.prev_Y

    def NewBorn(self, x, y):
        return Fox(self.world, x, y, self.generation + 1)
