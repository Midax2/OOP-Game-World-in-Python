from Game import Game


class Main:
    def main(self):
        game = Game()
        game.AddOrganismsToWorld()
        game.RunGame()


if __name__ == "__main__":
    main = Main()
    main.main()
