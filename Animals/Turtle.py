import random
from Animals.Animal import Animal


class Turtle(Animal):
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
        self.initiative = 1
        self.power = 2
        self.world = world
        self.identity = 'T'
        self.name = "Turtle"
        self.alive = True
        self.isMoving = False
        self.color = "DeepSkyBlue1"

    def Action(self):
        self.isMoving = False
        chance = random.randint(1, 4)
        if chance == 4:
            super().Action()
        self.isMoving = True

    def Collision(self, organism):
        if organism is None:
            return
        if not self.isMoving:
            organism.SetX(organism.GetPrevX())
            organism.SetY(organism.GetPrevY())
            message = f"{organism.GetName()} was pushed back to their previous position by Turtle at " \
                      f"X = {self.GetX()}, Y = {self.GetY()}"
            self.world.AddMessage(message)
        else:
            super().Collision(organism)
        self.isMoving = False

    def Defend(self, organism):
        return organism.GetPower() <= 5

    def NewBorn(self, X, Y):
        return Turtle(self.world, X, Y, self.generation + 1)

    def GetIsMoving(self):
        return self.isMoving

    def SetIsMoving(self, move):
        self.isMoving = move
