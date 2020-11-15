from tkinter import *
from neueGameObjects import Character, enemy, layer

class MainScreenWindow():
    
    def __init__(self):

        self.root = Tk()
        self.root.geometry("1200x675")
        self.root.title("GameTestName")
        self.fontSettings = ("Segoe UI", 12)

    def createMainScreenWindow(self):
        
        self.startGameButton = Button(self.root, text = "Start Game", width = 20, height = 2, bg = "lightgrey", command = lambda *args: self.createCharInterface())
        self.optionsButton = Button(self.root, text = "Options", width = 20, height = 2, bg = "lightgrey")
        self.exitButton = Button(self.root, text = "Exit", width = 20, height = 2, bg = "lightgrey", command = exit)

        self.startGameButton.place(x = 520, y = 200)
        self.optionsButton.place(x = 520, y = 240)
        self.exitButton.place(x = 520, y = 280)

        self.root.mainloop()

    def destroyButtonsMainScreenWindow(self):

        self.startGameButton.destroy()
        self.optionsButton.destroy()
        self.exitButton.destroy()

    def destroyButtonsCreateCharInterface(self):

        self.title.destroy()
        self.namensEingabe.destroy()
        self.namensEingabeText.destroy()
        self.charakterErstellenButton.destroy()
        self.exitButton2.destroy()

    def createCharInterface(self):

        self.destroyButtonsMainScreenWindow()

        self.title = Label(self.root, text = "Erstelle einen Charakter", font = ("Segoe UI", 15), width = 20, height = 2)

        self.namensEingabe = Entry(self.root, width = 20, font = ("", 15), bg = "lightblue")
        self.namensEingabeText = Label(self.root, text = "Name:", font = self.fontSettings)
        self.charakterErstellenButton = Button(self.root, text = "Erstellen", bg = "lightgreen", width = 20, height = 2, command = lambda *args: self.createGameMainScreenWindow())
        self.exitButton2 = Button(self.root, text = "Exit", width = 20, height = 2, bg = "lightgrey", command = exit)

        self.title.place(x = 500, y = 40)

        self.namensEingabe.place(x = 500, y = 100)
        self.namensEingabeText.place(x = 445, y = 101)
        self.charakterErstellenButton.place(x = 532, y = 140)
        self.exitButton2.place(x = 532, y = 180)

    def createGameMainScreenWindow(self):

        self.createCharacter()
        self.destroyButtonsCreateCharInterface()
        self.createCharacterSheet()
        self.testGame()

    def testGame(self):

        self.randomShitButton = Button(self.root, text = "LevelSex", command = lambda*args: self.testGame2())
        self.randomShitButton.place(x = 20, y = 300)

    def testGame2(self):

        self.player.levelUp()
        self.createCharacterSheet()

    def createCharacterSheet(self):
        
        try:
            self.destroyCharacterSheet()
        
        except:
            pass

        self.statArray = self.player.returnStats()

        self.playerInfoLabelName = Label(self.root, text = f"Name: {self.statArray[0]}", font = self.fontSettings)
        self.playerInfoLabelLevel = Label(self.root, text = f"Level: {self.statArray[1]}", font = self.fontSettings)
        self.playerInfoLabelHP = Label(self.root, text = f"Lebenspunkte: {self.statArray[2]} von {self.statArray[3]}", font = self.fontSettings)
        self.playerInfoLabelMP = Label(self.root, text = f"Mana: {self.statArray[4]} von {self.statArray[5]}", font = self.fontSettings)
        self.playerInfoLabelStrength = Label(self.root, text = f"Stärke: {self.statArray[6]}", font = self.fontSettings)
        self.playerInfoLabelDefense = Label(self.root, text = f"Verteidigung: {self.statArray[7]}", font = self.fontSettings)
        self.playerInfoLabelXP = Label(self.root, text = f"XP: {self.statArray[8]} von {self.statArray[9]}", font = self.fontSettings)
        
        self.exitButton3 = Button(self.root, text = "Exit", width = 20, height = 2, bg = "lightgrey", command = exit)
        
        self.playerInfoLabelName.place(x = 20, y = 30)
        self.playerInfoLabelLevel.place(x = 20, y = 55)
        self.playerInfoLabelHP.place(x = 20, y = 80)
        self.playerInfoLabelMP.place(x = 20, y = 105)
        self.playerInfoLabelStrength.place(x = 20, y = 130)
        self.playerInfoLabelDefense.place(x = 20, y = 155)
        self.playerInfoLabelXP.place(x = 20, y = 180)

        self.exitButton3.place(x = 1050, y = 634)


    def destroyCharacterSheet(self):

        self.playerInfoLabelName.destroy()
        self.playerInfoLabelLevel.destroy()
        self.playerInfoLabelHP.destroy()
        self.playerInfoLabelMP.destroy()
        self.playerInfoLabelStrength.destroy()
        self.playerInfoLabelDefense.destroy()
        self.playerInfoLabelXP.destroy()
        

    def createCharacter(self):

        nameInput = self.namensEingabe.get()
        if len(nameInput) == 0:
            nameInput = "Retard"

        self.player = Character(name = nameInput)

    def createFightEnemy(self):



        

    




        

        
        
        
MainScreenWindow().createMainScreenWindow()








