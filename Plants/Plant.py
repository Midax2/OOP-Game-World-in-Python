import random
from Organism import Organism


class Plant(Organism):
    def Action(self):
        possibility = random.randint(1, 9999)
        if possibility % 36 == 0:
            pos = random.randint(0, 8)
            count = 0
            for i in range(self.GetX() - 1, self.GetX() + 2):
                for j in range(self.GetY() - 1, self.GetY() + 2):
                    if self.GetWorld().GetElement(i, j) == ' ' and count == pos:
                        self.GetWorld().AddOrganism(self.NewBorn(i, j))
                        message = f"New {self.GetName()} was born at X = {j}, Y = {i}"
                        self.world.AddMessage(message)
                        return
                    count += 1

    def Collision(self, organism):
        if organism is None:
            return
        if organism.IsEatenDebuff(self.GetMe()):
            organism.Collision(self.GetMe())
            return
        if self.GetPower() > organism.GetPower():
            organism.GetWorld().DeleteOrganism(organism)
            message = f"{organism.GetName()} was killed by {self.GetName()} at X = {self.GetX()}, Y = {self.GetY()}"
            organism.SetAlive(False)
            self.world.AddMessage(message)
        else:
            self.GetWorld().DeleteOrganism(self.GetMe())
            message = f"{self.GetName()} was killed by {organism.GetName()} at X = {self.GetX()}, Y = {self.GetY()}"
            self.SetAlive(False)
            self.world.AddMessage(message)

    def NewBorn(self, X, Y):
        return None
