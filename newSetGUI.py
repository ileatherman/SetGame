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
    ourGame.firstDraw()
    displayHand()
    gameButt.configure(text="New Game")
    #start timer?
    return False

def displayHand():
    for i in range(12):
        name = ourGame.hand[i].imagename
        cardImages[name] = tk.PhotoImage(file=name)        
        displayedCardButtons[i].config(
            image = cardImages[name],
            text='',)
        bindButton(i)
        """
        func = make_bind_function(i)
        displayedCardButtons[i].bind(
            "<Button-1>",
            lambda event: func(event))
        """

""" 
TODO - delete these once i'm SURE i won't need them
def butt0(event):
    selectCard(0)
def butt1(event):
    selectCard(1) 
def butt2(event):
    selectCard(2)    
def butt3(event):
    selectCard(3)    
def butt4(event):
    selectCard(4)    
def butt5(event):
    selectCard(5)     
def butt6(event):
    selectCard(6)   
def butt7(event):
    selectCard(7)    
def butt8(event):
    selectCard(8)    
def butt9(event):
    selectCard(9)    
def butt10(event):
    selectCard(10)    
def butt11(event):
    selectCard(11)
"""
  
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
    
    
def make_bind_function(index):
    def bindFunc(event):
        return selectCard(event,index)
    return bindFunc
                 

def selectCard(event,index):
    """
    TODO - make sure card isn't selected already
    """ 
    if index in selectedCards:
        displayedCardButtons[index].config(bg="white")
        selectedCards.remove(index)
    else:
        selectedCards.append(index)
        displayedCardButtons[index].config(bg="purple")
    if len(selectedCards) < 3:
        return
    elif len(selectedCards) == 3:
        #time.sleep(0.5)
        checkSelection()
        clearSelection()
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
    #for index in selectedCards:
       # displayedCardButtons[index].config(bg="white")
    return

def setFalse():
    #for index in selectedCards:
    #    displayedCardButtons[index].config(bg="white")
    return

def clearSelection():
    for index in selectedCards:
        displayedCardButtons[index].config(bg="white")
    del selectedCards[:]

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
