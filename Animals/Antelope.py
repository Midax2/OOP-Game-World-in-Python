import random
from Animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, world, X=None, Y=None, generation=None):
        super().__init__()
        self.isRunning = False
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
        self.identity = 'A'
        self.name = "Antelope"
        self.alive = True
        self.color = "dark red"

    def Action(self):
        super().Action()
        rd = random.Random()
        if rd.randint(0, 1) == 1:
            super().Action()

    def Collision(self, organism):
        if organism is None:
            return
        if self.isRunning:
            if organism.GetPower() > self.GetPower():
                for i in range(self.GetY() - 1, self.GetY() + 2):
                    for j in range(self.GetX() - 1, self.GetX() + 2):
                        if self.world.GetElement(j, i) == ' ':
                            self.SetX(j)
                            self.SetY(i)
                            self.isRunning = False
                            message = "Antelope run away from " + organism.GetName() + " to X = " + str(
                                self.GetX()) + ", Y = " + str(self.GetY())
                            self.world.AddMessage(message)
                            return

    def GetIsRunning(self):
        return self.isRunning

    def SetIsRunning(self, run):
        self.isRunning = run

    def NewBorn(self, x, y):
        return Antelope(self.world, x, y, self.generation + 1)
