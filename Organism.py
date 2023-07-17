class Organism:
    def __init__(self):
        self.alive = None
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
        self.name = None
        self.generation = None
        self.identity = None
        self.prev_Y = None
        self.prev_X = None
        self.Y = None
        self.X = None
        self.power = None
        self.initiative = None
        self.color = None
        self.world = None

    def Action(self):
        pass

    def Collision(self, organism):
        pass

    def NewBorn(self, X, Y):
        pass

    def GetWorld(self):
        return self.world

    def GetMe(self):
        return self

    def GetColor(self):
        return self.color

    def GetInitiative(self):
        return self.initiative

    def GetPower(self):
        return self.power

    def SetPower(self, power):
        self.power = power

    def GetX(self):
        return self.X

    def GetY(self):
        return self.Y

    def SetX(self, X):
        self.X = X

    def SetY(self, Y):
        self.Y = Y

    def GetPrevX(self):
        return self.prev_X

    def GetPrevY(self):
        return self.prev_Y

    def SetPrevX(self, X):
        self.prev_X = X

    def SetPrevY(self, Y):
        self.prev_Y = Y

    def GetAlive(self):
        return self.alive

    def SetAlive(self, alive):
        self.alive = alive

    def GetIdentity(self):
        return self.identity

    def GetGeneration(self):
        return self.generation

    def GetName(self):
        return self.name

    def Defend(self, organism):
        return False

    def RunAway(self, organism):
        return False

    def IsEatenDebuff(self, organism):
        return False

    def Print(self):
        self.world.SetOrganismOnPoint(self.GetX(), self.GetY(), self.GetIdentity())
