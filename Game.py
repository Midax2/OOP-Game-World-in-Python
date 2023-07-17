import os
import random
import tkinter as tk
from tkinter import font, filedialog
from tkinter import ttk
from tkinter.tix import Tk
from Animals.Human import Human
from Animals.Fox import Fox
from Animals.Wolf import Wolf
from Animals.Sheep import Sheep
from Animals.CyberSheep import CyberSheep
from Animals.Turtle import Turtle
from Animals.Antelope import Antelope
from Plants.Dandelion import Dandelion
from Plants.Guarana import Guarana
from Plants.Heracleum import Heracleum
from Plants.Belladonna import Belladonna
from Plants.Grass import Grass
from World import World
from Turn import Turn
from Organisms_t import Organisms_t


class Game:
    def __init__(self):
        self.squareSize = 20
        self.width = 20
        self.height = 20
        self.player = None
        self.world = None
        self.panel = None
        self.root = None
        self.frame = tk.Tk()
        self.frame.title("Game")
        self.side_panel = None
        self.info = None
        self.StartGame()

    def StartGame(self):
        size_panel = tk.Frame(self.frame)
        width_label = tk.Label(size_panel, text="Width: ", font=font.Font(family='Arial', size=16))
        width_field = tk.Entry(size_panel, font=font.Font(family='Arial', size=16))
        height_label = tk.Label(size_panel, text="Height: ", font=font.Font(family='Arial', size=16))
        height_field = tk.Entry(size_panel, font=font.Font(family='Arial', size=16))
        size_panel.grid_columnconfigure(1, weight=1)
        width_label.grid(row=0, column=0, sticky="w")
        width_field.grid(row=0, column=1, sticky="we")
        height_label.grid(row=1, column=0, sticky="w")
        height_field.grid(row=1, column=1, sticky="we")
        size_panel.columnconfigure(0, weight=1)
        size_panel.columnconfigure(1, weight=1)
        size_panel.columnconfigure(2, weight=1)
        size_panel.rowconfigure(0, weight=1)
        size_panel.rowconfigure(1, weight=1)
        size_panel.rowconfigure(2, weight=1)
        size_panel.rowconfigure(3, weight=1)
        size_panel.rowconfigure(4, weight=1)
        size_panel.config(width=400, height=200)

        pressed = tk.BooleanVar(value=False)
        start_button = tk.Button(size_panel, text="Start",
                                 command=lambda: self.CreateWorld(int(width_field.get()), int(height_field.get()),
                                                                  pressed))
        start_button.config(font=font.Font(family='Arial', size=16))
        start_button.grid(row=2, column=0, columnspan=2, sticky="s")
        size_panel.pack(fill="both", expand=True, padx=20, pady=20)

        self.info = tk.Label(self.frame, text="")
        self.info.pack(side=tk.BOTTOM)

        while not pressed.get():
            self.frame.update()
        self.width = int(width_field.get())
        self.height = int(height_field.get())
        self.squareSize = 500 // self.width
        self.frame.destroy()

    def CreateWorld(self, width, height, pressed):
        self.world = World(width, height)
        self.player = Human(self.world)
        self.world.AddOrganism(self.player)
        self.AddSidePanels()
        self.frame.update()
        self.frame.geometry('')
        pressed.set(True)

    def AddSidePanels(self):
        self.root = Tk()
        frame = ttk.Frame(self.root)
        frame.place()
        self.panel = tk.Frame(self.root)
        self.panel.place(x=0, y=0)
        self.panel.config(bg="white")

        next_round_button = tk.Button(self.root, text="Next Round", command=lambda: self.NextRound())
        save_button = tk.Button(self.root, text="Save", command=lambda: self.Save())
        load_button = tk.Button(self.root, text="Load", command=lambda: self.Load())
        super_power_button = tk.Button(self.root, text="Use Super Power", command=lambda: self.UsePlayerPower())

        next_round_button.place(x=0, y=(self.height + 15) * self.squareSize)
        save_button.place(x=85, y=(self.height + 15) * self.squareSize)
        load_button.place(x=130, y=(self.height + 15) * self.squareSize)
        super_power_button.place(x=180, y=(self.height + 15) * self.squareSize)

        self.side_panel = tk.Canvas(self.root, bg="lightgray")
        self.side_panel.place(x=(self.width + 15) * self.squareSize, y=0, width=300, height=1000000)
        screenHeight = (self.height + 15) * self.squareSize + 50
        screenWidth = int(1.5 * (self.width + 15) * self.squareSize)
        self.root.geometry(f"{screenWidth}x{screenHeight}")

    def AddOrganismsToWorld(self):
        for organism in Organisms_t:
            random_num = random.randint(2, 10)
            for _ in range(random_num):
                if organism == Organisms_t.Wolf_t:
                    self.world.AddOrganism(Wolf(self.world))
                elif organism == Organisms_t.Turtle_t:
                    self.world.AddOrganism(Turtle(self.world))
                elif organism == Organisms_t.Sheep_t:
                    self.world.AddOrganism(Sheep(self.world))
                elif organism == Organisms_t.Fox_t:
                    self.world.AddOrganism(Fox(self.world))
                elif organism == Organisms_t.Antelope_t:
                    self.world.AddOrganism(Antelope(self.world))
                elif organism == Organisms_t.Belladonna_t:
                    self.world.AddOrganism(Belladonna(self.world))
                elif organism == Organisms_t.Dandelion_t:
                    self.world.AddOrganism(Dandelion(self.world))
                elif organism == Organisms_t.Grass_t:
                    self.world.AddOrganism(Grass(self.world))
                elif organism == Organisms_t.Guarana_t:
                    self.world.AddOrganism(Guarana(self.world))
                elif organism == Organisms_t.Heracleum_t:
                    self.world.AddOrganism(Heracleum(self.world))
                elif organism == Organisms_t.CyberSheep_t:
                    self.world.AddOrganism(CyberSheep(self.world))
        self.world.SortOrganisms()

    def RunGame(self):
        self.PrintInfo()
        self.PrintQuadWorld()
        self.root.mainloop()

    def NextRound(self):
        self.world.DoTurn()
        self.player.SetTurn(Turn.NONE)
        self.PrintQuadWorld()
        self.info.destroy()
        self.PrintInfo()
        self.world.ClearMessages()

    def UsePlayerPower(self):
        self.player.ChangeSuperPower()
        self.info.destroy()
        self.PrintInfo()
        self.world.ClearMessages()

    def PrintInfo(self):
        text = "Help:\n" \
               "Click on organism to see advanced info\n" \
               "Choose direction for human - Arrows / Mouse\n\n" \
               "Game status:\n" \
               "Player/Creator: Dmytro Dzhusov nr. 196751\n" \
               "Round: " + str(self.world.GetRound()) + "\n"
        if not self.player.GetAlive() or self.world.GetRound() <= self.player.GetEndRound():
            text += "Superpower is not available\n"
        else:
            text += "Superpower is available\n"
        text += "Turn : X = " + str(self.player.GetHexX()) + ", Y = " + str(self.player.GetHexY())

        logsText = "\n\nLogs:\n"
        i = 0
        while True:
            message = self.world.GetMessage(i)
            if message == "Nothing":
                break
            logsText += message + "\n"
            i += 1

        text += logsText

        self.info = tk.Label(self.side_panel, text=text, justify=tk.LEFT, anchor=tk.NW)
        self.info.pack()

    def PrintQuadWorld(self):
        for i in range(1, self.world.GetHeight() + 1):
            for j in range(1, self.world.GetWidth() + 1):
                organism = self.world.GetOrganism(None, j, i)
                square = tk.Canvas(self.panel, width=self.squareSize, height=self.squareSize, bg="white")
                if organism is not None:
                    color = organism.GetColor()
                    square.configure(bg=color)
                    square.bind("<Button-3>", lambda event, org=organism: self.ShowOrganismInfo(org, event))
                square.bind("<Button-1>", lambda event, ii=i, jj=j: self.ChoosePlayerLocation(event, ii, jj))
                square.grid(row=i, column=j, sticky="nsew")
        self.panel.update()

    def ChoosePlayerLocation(self, event, i, j):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        goodTurn = False

        for q in range(4):
            tempX = self.player.GetX() + dx[q]
            tempY = self.player.GetY() + dy[q]
            if j == tempX and i == tempY:
                goodTurn = True

        if (
                0 <= j <= self.world.GetWidth() and
                0 <= i <= self.world.GetHeight() and
                goodTurn is True
        ):
            self.player.SetHexX(j)
            self.player.SetHexY(i)
            self.info.destroy()
            self.PrintInfo()

    def ShowOrganismInfo(self, organism, event):
        info = f"{organism.GetName()} at X = {organism.GetX()} Y = {organism.GetY()}"
        x = event.widget.winfo_rootx() + event.widget.winfo_width()
        y = event.widget.winfo_rooty()

        info_window = tk.Toplevel(self.root)
        info_window.title("Organism Info")

        info_label = tk.Label(info_window, text=info, padx=10, pady=10)
        info_label.grid(row=0, column=0)

        ok_button = tk.Button(info_window, text="OK", command=info_window.destroy)
        ok_button.grid(row=1, column=0, pady=10)

        info_window.geometry(f"+{x}+{y}")
        info_window.grab_set()
        info_window.wait_window()

    def Save(self):
        save_window = tk.Toplevel(self.root)
        save_window.title("Save")
        label = tk.Label(save_window, text="Enter the name of the saved file:")
        label.pack()
        entry = tk.Entry(save_window)
        entry.pack()
        button = tk.Button(save_window, text="Save", command=lambda: self.PerformSave(entry.get(), save_window))
        button.pack()
        save_window.wait_window()

    def PerformSave(self, saveName, save_window):
        if saveName:
            saveName += ".save"
            try:
                with open(saveName, "w") as file:
                    orgs = self.world.GetOrganisms()
                    file.write(str(self.world.GetRound()) + " ")
                    file.write(str(self.world.GetHeight()) + " ")
                    file.write(str(self.world.GetWidth()) + " ")
                    file.write("\n")
                    for org in orgs:
                        file.write(org.GetIdentity() + " ")
                        file.write(str(org.GetX()) + " ")
                        file.write(str(org.GetY()) + " ")
                        file.write(str(org.GetGeneration()) + " ")
                        file.write(str(org.GetPower()) + " ")
                        if org.GetIdentity() == 'H':
                            file.write(str(org.GetSuperPower()) + " ")
                            file.write(str(org.GetEndRound()) + " ")
                        if org.GetIdentity() == 'A':
                            file.write(str(org.GetIsRunning()) + " ")
                        if org.GetIdentity() == 'T':
                            file.write(str(org.GetIsMoving()) + " ")
                        file.write("\n")
                    self.world.AddMessage("Save successful")
            except IOError as e:
                print("An error occurred while saving the file:", str(e))
        save_window.destroy()

    def Load(self):
        fileChooser = filedialog.askopenfile(initialdir=".", filetypes=[("Saved Files", "*.save")])
        if fileChooser:
            saveName = fileChooser.name
            try:
                with open(saveName, "r") as file:
                    lines = file.readlines()
                    line = lines.pop(0).strip()
                    parameters = line.split(" ")
                    round = int(parameters[0])
                    temp_h = int(parameters[1])
                    temp_w = int(parameters[2])

                    self.world = World(temp_w, temp_h)
                    self.squareSize = 500 // temp_w
                    self.world.SetRound(round)
                    self.panel.destroy()
                    self.panel = tk.Frame(self.root)
                    self.panel.place(x=0, y=0)
                    self.panel.config(bg="white")

                    for line in lines:
                        tokens = line.strip().split(" ")
                        identity = tokens[0]
                        X = int(tokens[1])
                        Y = int(tokens[2])
                        Gen = int(tokens[3])
                        Power = int(tokens[4])

                        if identity == 'H':
                            self.player = Human(self.world, X, Y, Gen)
                            self.world.AddOrganism(self.player)
                            self.player.SetPower(Power)
                            SuperPower = bool(tokens[5])
                            self.player.SetSuperPower(SuperPower)
                            endRound = int(tokens[6])
                            self.player.SetEndRound(endRound)
                        elif identity == 'W':
                            wolf = Wolf(self.world, X, Y, Gen)
                            self.world.AddOrganism(wolf)
                            wolf.SetPower(Power)
                        elif identity == 'A':
                            antelope = Antelope(self.world, X, Y, Gen)
                            self.world.AddOrganism(antelope)
                            antelope.SetPower(Power)
                            isRunning = bool(tokens[5])
                            antelope.SetIsRunning(isRunning)
                        elif identity == 'F':
                            fox = Fox(self.world, X, Y, Gen)
                            self.world.AddOrganism(fox)
                            fox.SetPower(Power)
                        elif identity == 'S':
                            sheep = Sheep(self.world, X, Y, Gen)
                            self.world.AddOrganism(sheep)
                            sheep.SetPower(Power)
                        elif identity == 'C':
                            cyberSheep = CyberSheep(self.world, X, Y, Gen)
                            self.world.AddOrganism(cyberSheep)
                            cyberSheep.SetPower(Power)
                        elif identity == 'T':
                            turtle = Turtle(self.world, X, Y, Gen)
                            self.world.AddOrganism(turtle)
                            turtle.SetPower(Power)
                            isMoving = bool(tokens[5])
                            turtle.SetIsMoving(isMoving)
                        elif identity == 'B':
                            belladonna = Belladonna(self.world, X, Y, Gen)
                            self.world.AddOrganism(belladonna)
                        elif identity == 'D':
                            dandelion = Dandelion(self.world, X, Y, Gen)
                            self.world.AddOrganism(dandelion)
                        elif identity == 'G':
                            grass = Grass(self.world, X, Y, Gen)
                            self.world.AddOrganism(grass)
                        elif identity == 'U':
                            guarana = Guarana(self.world, X, Y, Gen)
                            self.world.AddOrganism(guarana)
                        elif identity == 'M':
                            heracleum = Heracleum(self.world, X, Y, Gen)
                            self.world.AddOrganism(heracleum)

                    self.world.AddMessage("Load successful")
                    self.PrintQuadWorld()
                    self.info.destroy()
                    self.PrintInfo()
            except IOError as e:
                print("An error occurred while loading the file:", str(e))

