# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:05:45 2020

@author: mriou
"""

from tkinter import *
from tkinter import PhotoImage
from random import randint,choice
from string import ascii_uppercase

def word_choice():
    global words
    R=randint(0,len(words)-1)
    tobeguessedword=words[R]
    return tobeguessedword

def play(l):
    global propositions,erreur,tobeguessedword,guessword,photos,imgLabel
    l=l.lower()
    if l in propositions:
        print("already proposed")
    else:
        propositions.append(l)
        if l not in tobeguessedword:
            erreur+=1
            imgLabel.config(image=photos[erreur])  
            if erreur==len(photos)-1:
                guessword.set("")
                print("Le mot était ",tobeguessedword)
                reset()
                          
        else:
            guessword.set(check(guessword.get(),tobeguessedword,propositions))
            if(guessword.get().replace(" ","")==tobeguessedword):
                guessword.set("")
                print("Vous avez gagné")
                reset()
            
def check(guessword,tobeguessedword,propositions):
    guessword=""
    for i in range(len(tobeguessedword)):
        if tobeguessedword[i] in propositions:
            guessword+=tobeguessedword[i]+" "
        else:
            guessword+="_ "
    return guessword
    
def reset():
    global propositions,tobeguessedword,erreur,guessword,imgLabel
    tobeguessedword=choice(words)
    propositions=[]
    erreur=0
    guessword=StringVar(value="_ "*len(tobeguessedword))
    Label(window,textvariable=guessword, font=("Consolas 24 bold")).grid(row=0, column=3,columnspan=6,padx=10)
    imgLabel=Label(window)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0])

def main():
    global photos,window,words,Score
    
    file= open("mots.txt")
    words=file.read().split(" ")
    
    window=Tk()
    window.title("Hangman Game")
    
    Score=IntVar(value=0)
    
    n=0
    for c in ascii_uppercase:
        Button(window,text=c, command=lambda c=c:play(c), font=("Helvetica 10"), width=4).grid(row=2+n//9, column=n%9)
        n+=1
    
    photos=[PhotoImage(file="images/hang0.png"),PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),
            PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),
            PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png"),PhotoImage(file="images/hang8.png"),
            PhotoImage(file="images/hang9.png"),PhotoImage(file="images/hang10.png"),PhotoImage(file="images/hang11.png")]
   
    reset()
    
    window.mainloop()

    
if __name__=='__main__':
    main()