import random
from Plants.Plant import Plant


class Heracleum(Plant):
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
        self.power = 10
        self.world = world
        self.identity = 'M'
        self.name = "Heracleum"
        self.alive = True
        self.color = "SeaGreen3"

    def Action(self):
        for i in range(self.GetY() - 1, self.GetY() + 2):
            for j in range(self.GetX() - 1, self.GetX() + 2):
                org = self.world.GetOrganism(self.GetMe(), j, i)
                if org is not None and 0 < org.GetPower() < self.power:
                    org.SetAlive(False)
                    self.world.DeleteOrganism(org)

    def Collision(self, organism):
        if organism is None:
            return
        organism.SetAlive(False)
        self.SetAlive(False)
        self.world.DeleteOrganism(self.GetMe())
        if self.power >= organism.GetPower():
            self.world.DeleteOrganism(organism)
            message = organism.GetName() + " dead after eating Heracleum at X = " + str(self.X) + " Y = " + str(self.Y)
        else:
            message = "Heracleum was eaten by Cyber Sheep at X = " + str(self.X) + " Y = " + str(self.Y)
        self.world.AddMessage(message)

    def NewBorn(self, x, y):
        return Heracleum(self.world, x, y, self.generation + 1)

    def IsEatenDebuff(self, organism):
        return True
