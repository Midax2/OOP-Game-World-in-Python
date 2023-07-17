import random
from Plants.Plant import Plant


class Belladonna(Plant):
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
        self.initiative = 0
        self.power = 0
        self.world = world
        self.identity = 'U'
        self.name = "Guarana"
        self.alive = True
        self.color = "#146464"

    def Collision(self, organism):
        if organism is None:
            return
        organism.SetAlive(False)
        self.SetAlive(False)
        self.world.DeleteOrganism(self.GetMe())
        self.world.DeleteOrganism(organism)
        message = organism.GetName() + " dead after eating Belladonna at X = " + str(self.X) + " Y = " + str(self.Y)
        self.world.AddMessage(message)

    def NewBorn(self, x, y):
        return Belladonna(self.world, x, y, self.generation + 1)

    def IsEatenDebuff(self, organism):
        return True
