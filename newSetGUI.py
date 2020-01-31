#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:46:42 2020

@author: Isabel
"""

import tkinter as tk
from tkinter import ttk
import setGame as sg
import time  
from PIL import ImageTk

ourGame = sg.setGame()
displayedCardButtons = []
selectedCards = []

def newGame():
    ourGame.startGame()
    ourGame.firstDraw()
    displayHand()
    gameButt.configure(text="New Game")
    #start timer?
    return False

def displayHand():
    for i in range(12):
        print('in display hand')
        displayedCardButtons[i].configure(
            image = ImageTk.PhotoImage(ourGame.hand[i].image),
            command = lambda: selectCard(i))

def selectCard(index): 
    """
    TODO - make sure card isn't selected already

    """
    if len(selectedCards) < 3:
        selectedCards.push(index)
    elif len(selectedCards) == 3:
        checkSelection()
    else:
        """ 
        TODO - should throw an error here
        """
        return

def checkSelection():
    a = ourGame.hand[selectedCards[0]]
    b = ourGame.hand[selectedCards[1]]
    c = ourGame.hand[selectedCards[2]]
    isSet = ourGame.checkSet(a,b,c)
    if isSet:
        setTrue()
    else:
        setFalse()
    
def setTrue():
    return

def setFalse():
    return

def quitandclose():
    root.destroy()
    tk.sys.exit()   

root = tk.Tk()
root.title("SET")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Import empty card image
emptyCard = tk.PhotoImage(file='cards/card.png')

content = ttk.Frame(root)
content.grid(row=0, column=0, sticky=('N', 'S', 'E', 'W'))

hand = ttk.Frame(content, borderwidth=5, relief='sunken',padding=3)
hand.grid(row=0, column=0, rowspan=3)

r = 0
c = 0
for i in range(12):
    string = "Card " + str(i+1)
    b = tk.Button(
        hand,
        text=string,
        image=emptyCard,
        compound="center",
        height = 150, width = 233)
    b.grid(row=r,column=c,padx=3,pady=3)
    displayedCardButtons.append(b)
    c += 1
    if c == 3:
        r += 1
        c = 0

# Deck widget        
deck = ttk.Frame(content)
deck.grid(row=0, column=1)

deckLab = ttk.Label(deck, text='Deck', image=emptyCard, compound="center")
deckLab.grid(row=0, column=0, padx=10)

# High Score Widget
highScores = ttk.LabelFrame(
    content, 
    text='Fastest Times', 
    width=233, height=100)
highScores.grid(row=1, column=1)
highScores.columnconfigure(0, weight=1) #keeps label centered


"""
TODO write a method to read high scores from a CSV document or something
to display
"""
fastTimesText = "AAA 00:00\nAAA 00:00\nAAA 00:00"
fastTimes = ttk.Label(highScores, text = fastTimesText)
fastTimes.grid(row=0,column=0)

"""
fastInits = "TEST\nTEST\nTEST"
fastTimes = "00:00\n00:00\n00:00"

initials = ttk.Label(highScores, text = fastInits, anchor = 'w')
initials.grid(row=0,column=0)

times = ttk.Label(highScores, text = fastTimes, anchor='e')
times.grid(row=0,column=1)
 """  
# Game Buttons
gameButtons = ttk.Frame(content, height=30)
gameButtons.grid(row=2, column=1)
gameButtons.columnconfigure(0, weight=1)

gameButt = tk.Button(
    gameButtons,
    text="Start Game",
    command = newGame,
    pady=5,
    width = 15)
gameButt.grid(row=0, column=0)

rulesButt = tk.Button(
    gameButtons,
    text="How To Play",
    pady=5,
    width=15)
    #height = 25, width = 100)
rulesButt.grid(row=1, column=0)

"""
TODO the quit button doesn't work for some reason
"""
quitButt = tk.Button(
    gameButtons,
    text="QUIT",
    fg="red",
    command= root.destroy,
    pady=5,
    width=15)
   # height = 25, width=100)
quitButt.grid(row=2,column=0)

content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)

root.mainloop()
