from random import randint, choice
from Organism import Organism
from Turn import Turn


class Animal(Organism):
    def Action(self):
        self.SetPrevX(self.GetX())
        self.SetPrevY(self.GetY())
        self.world.SetOrganismOnPoint(self.GetX(), self.GetY(), ' ')

        if self.world.GetType() == "Quad":
            number = list(Turn)
            turn = choice(number)
            if turn == Turn.LEFT and self.GetX() - 1 >= 1:
                self.SetX(self.GetX() - 1)
            elif turn == Turn.UP and self.GetY() - 1 >= 1:
                self.SetY(self.GetY() - 1)
            elif turn == Turn.RIGHT and self.GetX() + 1 <= self.world.GetWidth():
                self.SetX(self.GetX() + 1)
            elif turn == Turn.DOWN and self.GetY() + 1 <= self.world.GetHeight():
                self.SetY(self.GetY() + 1)
        else:
            turn = randint(0, 5)
            x = self.GetX() + self.dx[turn]
            y = self.GetY() + self.dy[turn]
            if 1 <= x <= self.world.GetWidth() and 1 <= y <= self.world.GetHeight():
                self.SetX(x)
                self.SetY(y)

    def Collision(self, organism):
        if organism is None:
            return

        if self.GetIdentity() == organism.GetIdentity():
            if self.GetGeneration() != organism.GetGeneration():
                return

            self.SetX(self.GetPrevX())
            self.SetY(self.GetPrevY())

            if self.world.GetType() == "Quad":
                for i in range(self.GetX() - 1, self.GetX() + 2):
                    for j in range(self.GetY() - 1, self.GetY() + 2):
                        if self.world.GetElement(i, j) == ' ':
                            self.world.AddOrganism(self.NewBorn(i, j))
                            message = f"New {self.GetName()} was born at X = {j}, Y = {i}"
                            self.world.AddMessage(message)
                            return
            else:
                for i in range(6):
                    x = self.GetX() + self.dx[i]
                    y = self.GetY() + self.dy[i]
                    if self.world.GetElement(x, y) == ' ':
                        self.world.AddOrganism(self.NewBorn(x, y))
                        message = f"New {self.GetName()} was born at X = {x}, Y = {y}"
                        self.world.AddMessage(message)
                        return
        else:
            if organism.IsEatenDebuff(self.GetMe()):
                organism.Collision(self.GetMe())
                return

            if self.GetPower() >= organism.GetPower():
                if organism.Defend(self.GetMe()):
                    organism.Collision(self.GetMe())
                    return

                organism.SetAlive(False)
                self.world.DeleteOrganism(organism)
                message = f"{organism.GetName()} was killed by {self.GetName()} at X = {self.GetX()}, Y = {self.GetY()}"
                self.world.AddMessage(message)
            else:
                if self.RunAway(organism):
                    self.GetMe().collision(organism)
                    return

                self.world.DeleteOrganism(self.GetMe())
                self.SetAlive(False)
                message = f"{self.GetName()} was killed by {organism.GetName()} at X = {self.GetX()}, Y = {self.GetY()}"
                self.world.AddMessage(message)

    def NewBorn(self, x, y):
        return None
