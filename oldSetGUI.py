# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:38:09 2019

@author: Isabel
"""

"""
This was originally written with Python 2.7, and I switched over to Python 3.7 
because Python 2.7 is obsolete now. Big thanks to my Physics professors who 
refuse to update lab materials for Python 2.7 for why it took me so long to 
switch over. Anyways, when coming back to this project, I decided on so many 
fundamental changes to the setup that I've ended up writing an entirely new 
GUI from scratch instead, but I'm keeping this up as a reference for myself
I guess? I don't know why anyone else would read this anyway so I don't know 
why I'm justifying my decisions.

Oh I should also note that this was written with python 3.7.0 because running 
it with Python 3.7.6 with macOS Mojave kept crashing my computer. Thanks, 
Steve. He's a terrible enough person that I feel comfortable blaming him for
every issue I encounter.
"""

import tkinter as tk
import setGame
import tkinter.simpledialog
    
class newGameDialog(tkinter.simpledialog.Dialog):
    
    def body(self, master):
        self.entries = []
        
        msg = tk.Label(master, text = "Please enter the names of the people who are playing.")
        msg.grid(row=0,column=0,columnspan=4)
    
        for i in range(1,5):
            playerNum = "Player " + str(i) + ": "
            label = tk.Label(master,text=playerNum)
            label.grid(row=i,column=0)
            e = tk.Entry(master)
            e.grid(row = i, column = 1)
            self.entries.append(e)
            
        return self.entries[0]
        
    def apply(self):       
        self.playerNames = []        
        
        for i in range(4):
            name = self.entries[i].get()
            if name != "":
                self.playerNames.append(name)
    
    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="Start Game", command=self.ok, default="active")
        w.pack(side="left", padx=5, pady=5)
        w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side="left", padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

def newGame():        
    
    playNamesTop = newGameDialog(root,title="New Game")
    
    players = playNamesTop.playerNames

    numPlayers = len(players)    
    
    playerPoints = [tk.IntVar() for _ in range(numPlayers)]
    
    # replace old names
    for widget in points.winfo_children():
        widget.destroy()
        
    r = 0
    for i in range(numPlayers): 
        text=players[i]+":"
        p = tk.Label(points,text=text).grid(row=r, column=0)
        playerPoints[i].set(0)
        pp = tk.Label(points,textvariable=playerPoints[i]).grid(row=r,column=1,padx=5)
        r += 1
        
    game = setGame(numPlayers)
    game.startGame()
    
    displayHand(game.hand)
    return
    
def quitandclose():
    root.destroy()
    #sys.exit()
    
def displayHand(hand):
    for card in hand:
        name = getCardImage(card)
        
        
def getCardImage(card):
    if card.colour == 'red':
        colour = 'r'
    elif card.colour == 'green':
        colour='g'
    elif card.colour == 'purple':
        colour = 'p'
    
    if card.shape == 'oval':
        shape = 'o'
    elif card.shape == 'diamond':
        shape = 'd'
    elif card.shape == 'squiggle':
        shape = 's'
    
    if card.number == 1:
        number = '1'
    elif card.number == 2:
        number = '2'
    elif card.number == 3:
        number = '3'
        
    if card.fill == 'empty':
        fill = 'e'
    elif card.fill == 'full':
        fill = 'f'
    elif card.fill == 'striped':
        fill = 's'
        
    return colour + shape + number + fill + ".gif"

# Creating Root GUI
root = tk.Tk()
root.title("SET")

# Importing All Image Files
card = tk.PhotoImage(file='cards/card.png')

hand = tk.Frame(root)
hand.grid(row = 0,column = 0,rowspan=3)

cards = []

#initializing variables for selected cards and IntVar storing selected cards
selectedCards = []
var = [tk.IntVar() for _ in range(12)]

#create Button instances for all 12 cards

r = 0
c = 0
for i in range(12):
    string = "Card " + str(i+1)
    b = tk.Checkbutton(
        hand,
        variable=var[i],
        text=string,
        image=card,
        compound="center",
        padx=1,
        pady=1,
        indicatoron=False)
    cards.append(b)
    cards[i].grid(row=r,column=c)
    c += 1
    if c == 4:
        r += 1
        c = 0

deck = tk.Frame(root)
deck.grid(row=0,column=1)

deckLab = tk.Label(deck,text="Deck",image=card,compound="center")
deckLab.grid(row=0,column=0,padx=50)

points = tk.LabelFrame(root,text="Points")
points.grid(row=1,column=1)

gameButtons = tk.Frame(root)
gameButtons.grid(row=2,column=1)

newGameButt = tk.Button(gameButtons,text="New Game",command=newGame)
newGameButt.grid(row=0,column=0)

quitButt = tk.Button(gameButtons,text="QUIT", fg="red", command=quitandclose)
quitButt.grid(row=0,column=1)



root.mainloop()