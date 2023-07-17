import random
from Animals.Animal import Animal


class CyberSheep(Animal):
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
        self.power = 11
        self.world = world
        self.identity = 'C'
        self.name = "Cyber Sheep"
        self.alive = True
        self.color = "pink"

    def Action(self):
        nextX = 0
        nextY = 0
        distance = 1000000
        for i in range(4):
            tempX = self.X + self.dx[i]
            tempY = self.Y + self.dy[i]
            organisms = self.world.GetOrganisms()
            for organism in organisms:
                if organism.GetIdentity() == 'M' and distance > ((tempX - organism.GetX()) * (tempX - organism.GetX()) + (tempY - organism.GetY()) * (tempY - organism.GetY())):
                    distance = ((tempX - organism.GetX()) * (tempX - organism.GetX()) + (tempY - organism.GetY()) * (tempY - organism.GetY()))
                    nextX = tempX
                    nextY = tempY
        if nextX == 0 and nextY == 0:
            super().Action()
        else:
            self.X = nextX
            self.Y = nextY

    def NewBorn(self, x, y):
        return CyberSheep(self.world, x, y, self.generation + 1)
