# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:41:22 2019

@author: Isabel
"""

import random as r
import numpy as np
import itertools as itert
import time
from PIL import Image

colours = ['red','green','purple']
shapes = ['oval','diamond','squiggle']
numbers = ['1','2','3']
fills = ['empty','full','striped']

class setCard:  
    def __init__(self,c,s,n,f):
        self.imagename = 'cards/'
        if c in colours:
            self.colour = c
            self.imagename += c[0]
        if s in shapes:
            self.shape = s
            self.imagename += s[0]
        if n in numbers:
            self.number = n
            self.imagename += n[0]
        if f in fills:
            self.fill = f
            self.imagename += f[0]
        self.imagename += '.png'
          
    # for testing    
    def showCard(self):
        print(self.number,self.colour,self.shape,self.fill)

class setDeck:
    def __init__(self):
        self.deck = []
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    for u in range(0,3):
                        card = setCard(colours[i],shapes[j],numbers[k],fills[u])
                        self.deck.append(card)
        
    def shuffleDeck(self):
        r.shuffle(self.deck)
        
    def emptyDeck(self):
        if self.deck == []:
            return True
        else:
            return False
        
    def drawCard(self):
        if self.emptyDeck() == False:
            return self.deck.pop(0)

class setGame:
    def __init__(self):
        self.deck = setDeck()
        self.hand = []
        
    def dispHand(self):
        for i in self.hand:
            print(i.number,i.shape,i.colour,i.fill)
        
    def firstDraw(self):
        self.deck.shuffleDeck()
        for i in range(0,12):
            self.hand.append(self.deck.drawCard())
     
    def replaceSet(self, indices):
        for index in indices:
            self.hand[index] = self.deck.drawCard()
    
    def removeSet(self, indices):
        for index in sorted(indices, reverse=True):
            del self.hand[index]
           
    def checkColours(self,a,b,c):
        acolour = a.colour
        bcolour = b.colour
        ccolour = c.colour
        if (( acolour == bcolour == ccolour) or (acolour != bcolour != ccolour)):
            return True
        else:
            return False

    def checkShapes(self,a,b,c):
        ashape = a.shape
        bshape = b.shape
        cshape = c.shape
        if (( ashape == bshape == cshape) or (ashape != bshape != cshape)):
            return True
        else:
            return False
            
    def checkNum(self,a,b,c):
        anum = a.number
        bnum = b.number
        cnum = c.number
        if (( anum == bnum == cnum) or (anum != bnum != cnum)):
            return True
        else:
            return False 
            
    def checkFills(self,a,b,c):
        afill = a.fill
        bfill = b.fill
        cfill = c.fill
        if (( afill == bfill == cfill) or (afill != bfill != cfill)):
            return True
        else:
            return False 
    
    def checkSet(self,a,b,c):
        isSet = False
        if (self.checkColours(a,b,c)
                and self.checkShapes(a,b,c) 
                and self.checkNum(a,b,c) 
                and self.checkFills(a,b,c) ):
            isSet = True
        return isSet
    
    # Checks the board to make sure there is at least one set possible
    def checkBoard(self): 
        for i in itert.combinations(self.hand,3):
            if self.checkSet(i[0],i[1],i[2]):
                return True
        return False
        
    def extraCard(self):
        if self.checkBoard() == 0:
            print('There are no sets in the hand. Adding an extra card.')
            self.hand.append(self.deck.drawCard())
                
    def startGame(self):      
        self.deck = setDeck()
        self.hand = []        
        #startTime = time()
        self.firstDraw()
        
    def newHand(self):
        for card in self.hand:
            self.deck.append(card)
        self.firstDraw()
        
        
        