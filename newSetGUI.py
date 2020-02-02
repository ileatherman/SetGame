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

ourGame = sg.setGame()
displayedCardButtons = []
selectedCards = []
cardImages = {}

def newGame():
    ourGame.startGame()
    while not ourGame.checkBoard():
        ourGame.newHand()
    displayHand()
    gameButt.configure(text="New Game")
    #start timer?
    return False

def displayHand():
    if not ourGame.checkBoard():
        noticeLabel.config(fg="black",text="No SETs possible, redrawing board.")
    while not ourGame.checkBoard():
        ourGame.newHand()
    i=0
    for card in ourGame.hand:
        name = card.imagename
        cardImages[name] = tk.PhotoImage(file=name)        
        displayedCardButtons[i].config(
            image = cardImages[name],
            text='',)
        bindButton(i)
        i+=1
    if i < 12:
        for j in range(i,12):
            displayedCardButtons[j].config(
                image=emptyCard)
            displayedCardButtons[j].unbind("<Button-1>")
  
def bindButton(index):
    switcher = {
        0: lambda event: selectCard(event,0),
        1: lambda event: selectCard(event,1),
        2: lambda event: selectCard(event,2),
        3: lambda event: selectCard(event,3),       
        4: lambda event: selectCard(event,4),       
        5: lambda event: selectCard(event,5),       
        6: lambda event: selectCard(event,6),
        7: lambda event: selectCard(event,7),
        8: lambda event: selectCard(event,8),
        9: lambda event: selectCard(event,9),
        10: lambda event: selectCard(event,10),
        11: lambda event: selectCard(event,11)
    }
    displayedCardButtons[index].bind(
        "<Button-1>",
        switcher[index]
        )   
    
def selectCard(event,index):
    if len(selectedCards)==3:
        clearSelection()
    if index in selectedCards:
        displayedCardButtons[index].config(bg="white")
        selectedCards.remove(index)
    else:
        selectedCards.append(index)
        displayedCardButtons[index].config(bg="purple")
    if len(selectedCards) < 3:
        return
    elif len(selectedCards) == 3:
        checkSelection()
    else:
        clearSelection()
        return
        
def checkSelection():
    #time.sleep(0.5)
    a = ourGame.hand[selectedCards[0]]
    b = ourGame.hand[selectedCards[1]]
    c = ourGame.hand[selectedCards[2]]
    isSet = ourGame.checkSet(a,b,c)
    if isSet:
        setTrue()
    else:
        setFalse()
    
def setTrue():
    noticeLabel.config(fg="purple",text="SET!")
    for index in selectedCards:
        displayedCardButtons[index].config(image=emptyCard,bg="white")
    time.sleep(0.3)
    if not ourGame.deck.emptyDeck():
        ourGame.replaceSet(selectedCards)
        displayHand()
    else:
        ourGame.removeSet(selectedCards)
        checkGameOver()
        #displayReducedHand()

def checkGameOver():
    if ourGame.checkBoard():
        displayHand()
    else:
        noticeLabel.config(fg="purple", text="Game Over!")
        gameButt.config(text="Start Game")
        for button in displayedCardButtons:
            button.config(image=emptyCard)
            button.unbind("<Button-1>") #may have issues here
            #button.bind("<Button-1>", lambda: ) #possible solution?

def setFalse():
    noticeLabel.config(fg="red", text="Not a SET")
    #for index in selectedCards:
    #    displayedCardButtons[index].config(bg="white")
    return

def clearSelection():
    for i in range(3):
        displayedCardButtons[selectedCards[i]].config(bg="white")
    del selectedCards[:3]
    noticeLabel.config(text="")

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

gameBoard = ttk.Frame(content)
gameBoard.grid(row=0, column=0, rowspan=3)

noticeLabel = tk.Label(gameBoard, width=15,relief="ridge")
noticeLabel.grid(row=0, column=0,pady=10)

hand = ttk.Frame(gameBoard, borderwidth=5, relief='sunken',padding=3)
hand.grid(row=1, column=0)

r = 0
c = 0
for i in range(12):
    string = "Card " + str(i+1)
    b = tk.Label(
        hand,
        image=emptyCard,
        height = 154, width = 237)
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
