from typing import List


class World:
    def __init__(self, width: int, height: int):
        self.round = 1
        self.type = "Quad"
        self.height = height
        self.width = width
        self.worldBoard = [[' '] * (width + 2) for _ in range(height + 2)]
        for i in range(height + 2):
            for j in range(width + 2):
                if i == 0 or i == height + 1:
                    self.worldBoard[i][j] = '-'
                elif j == 0 or j == width + 1:
                    self.worldBoard[i][j] = '|'
        self.organisms = []
        self.messages = []

    def SetOrganismOnPoint(self, X: int, Y: int, identity: str):
        self.worldBoard[Y][X] = identity

    def SortOrganisms(self):
        self.organisms.sort(key=lambda organism: (-organism.GetInitiative(), -organism.GetGeneration()))

    def ClearBoard(self):
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.worldBoard[i][j] = ' '

    def DoTurn(self):
        for i in range(len(self.organisms) - 1, -1, -1):
            organism = self.organisms[i]
            organism.Action()
            organism.Collision(self.GetOrganism(organism, organism.GetX(), organism.GetY()))
        self.ClearBoard()
        for org in self.organisms:
            org.Print()
        self.round += 1
        self.SortOrganisms()

    def GetType(self):
        return self.type

    def DeleteOrganism(self, something):
        self.organisms.remove(something)

    def AddOrganism(self, something):
        something.Print()
        self.organisms.append(something)

    def GetElement(self, X: int, Y: int) -> str:
        return self.worldBoard[Y][X]

    def GetOrganisms(self) -> List:
        return self.organisms

    def AddMessage(self, message: str):
        self.messages.append(message)

    def GetMessage(self, index: int) -> str:
        if index >= len(self.messages):
            return "Nothing"
        return self.messages[index]

    def ClearMessages(self):
        self.messages.clear()

    def GetOrganism(self, organismTest, X: int, Y: int):
        for organism in self.organisms:
            if organism.GetX() == X and organism.GetY() == Y and organism != organismTest:
                return organism
        return None

    def GetHeight(self) -> int:
        return self.height

    def GetWidth(self) -> int:
        return self.width

    def GetRound(self) -> int:
        return self.round

    def SetRound(self, round: int):
        self.round = round
