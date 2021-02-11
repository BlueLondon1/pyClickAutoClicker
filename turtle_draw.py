from turtle import *

def carre(taille, couleur):
    
    "fonction qui permet de dessiner un carré de taéille et de couleur determinées"
    color(couleur)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c = c+1
        