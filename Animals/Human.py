import random
from Animals.Animal import Animal
from Turn import Turn


class Human(Animal):
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
        self.hex_x = self.X
        self.hex_y = self.Y
        self.super_power = False
        self.super_power_end_round = -1
        self.initiative = 4
        self.power = 5
        self.world = world
        self.identity = 'H'
        self.name = "Human"
        self.alive = True
        self.color = "red"

    def Action(self):
        self.SetPrevX(self.GetX())
        self.SetPrevY(self.GetY())
        self.world.SetOrganismOnPoint(self.GetX(), self.GetY(), ' ')

        self.SetX(self.GetHexX())
        self.SetY(self.GetHexY())

    def Collision(self, organism):
        if self.super_power and self.world.GetRound() <= self.super_power_end_round:
            self.power += 5
            self.super_power = False
            super().Collision(organism)
            return

        if self.world.GetRound() <= self.super_power_end_round:
            self.power -= 1

        super().Collision(organism)

    def SetTurn(self, turn):
        self.turn = turn

    def GetTurn(self):
        return self.turn

    def SetHexX(self, x):
        self.hex_x = x

    def GetHexX(self):
        return self.hex_x

    def SetHexY(self, y):
        self.hex_y = y

    def GetHexY(self):
        return self.hex_y

    def ChangeSuperPower(self):
        if not self.super_power and self.world.GetRound() > self.super_power_end_round:
            self.super_power = True
            self.super_power_end_round = self.world.GetRound() + 5

    def NewBorn(self, x, y):
        return Human(self.world, x, y, self.generation + 1)

    def GetSuperPower(self):
        return self.super_power

    def SetSuperPower(self, power):
        self.super_power = power

    def GetEndRound(self):
        return self.super_power_end_round

    def SetEndRound(self, end_round):
        self.super_power_end_round = end_round
