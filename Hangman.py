# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:55:49 2018

@author: matthieu.rioual
"""

from random import randint
#ficher= open("ficher_tp2")
#mot=ficher.read().split(" ")
mot="bonjour la mif".split(" ")


dessins=[
""" 




  -----""",
  """
  
    |
    |
    |
  -----
  """,
  """
    _____
    |
    |
    |
    |
  -----
  """,
  """
    _____
    |  |
    |
    |
    |
  ----- 
  """,
  """
    _____
    |  |
    |  O
    |
    |
  -----
  """,
  """
    _____
    |  |
    |  O__
    |
    |
  -----
  """,
  """
   _____
    |  |
    |__O__
    |
    |
  -----
  """,
  """
   _____
    |  |
    |__O__
    |  |
    |
  -----
  """,
  """
   _____
    |  |
    |__O__
    |  |
    | /
  -----
  """,
  """
   _____
    |  |
    |__O__
    |  |
    | / \\
  -----
  """
  ]
    
#choose a word in the list
def word_choice():
    R=randint(0,len(mot)-1)
    tobeguessedword=mot[R]
    return tobeguessedword
  
#read the input until it s valid char  
def read(propositions):
    while True:
        l=str(input("Propose a letter : ")).lower()
        if (l.isalpha() and len(l)==1):
            if l in propositions:
                print("already proposed")
            else:
                propositions.append(l)
                break
        else:
            print("You have to give one and only one char")
            continue
    return propositions
       

def check(propositions,tobeguessedword):
    guessword=""
    for i in range(len(tobeguessedword)):
        if tobeguessedword[i] in propositions:
            guessword+=tobeguessedword[i]+" "
        else:
            guessword+="_ "

    return(guessword)
    
def show(guessword,erreur):
    print(dessins[erreur]+"\n")
    print(guessword)
    
        
def game():
    
    #initialisation
    tobeguessedword=word_choice()
    propositions=[]
    erreur=0
    guessword="_ "*len(tobeguessedword)
    show(guessword,erreur)


    #loop for the game
    while(tobeguessedword!=guessword.replace(" ","") and erreur<len(dessins)-1):
        propositions=read(propositions)
        print("Proposition already done ",propositions)
        if propositions[-1] not in tobeguessedword:
            erreur+=1
        else:
            guessword=check(propositions,tobeguessedword)
        #display the results
        show(guessword,erreur)
    
    #end of the game, either defeat or victory
    if erreur==len(dessins)-1:
        print("Unfortunately, you did'nt found the mistery word which was : ",tobeguessedword)
        return 0
    else:
        print('Congrats, you found the mistery word')
        return len(tobeguessedword)*100
    
def main():
    nb_game=0
    score=0
    flag=True
    while(flag==True):
        nb_game+=1
        score+=game()
        try:
            again=int(input("Enter 1 for a new game, 0 to quit : "))
        except:
            print()
        if again==0:
            flag=False
    print ("You played ",nb_game," games and you earn  ",score," points")
    
main()