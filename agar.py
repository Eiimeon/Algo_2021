from turtle import*
from math import sqrt
import random as rd


################Exercice 1 :

#Dé comenter cette tortue pour toutes les fonctions utilisant une tortue
#T=Turtle()

def carre(T,size):
    for i in range(4):
        T.forward(size)
        T.left(90)

#carre(T,100)


def cercle(T,radius):
    T.circle(radius)

#cercle(T,100)


################Exercice 2 :

'''T.speed(100)
T.penup()
T.setpos(0,-500)
T.pendown()'''


def escargotCarre(T,size,steps):
    delta=size/steps
    while size > 0 :
        T.forward(size)
        T.left(90)
        size -= delta

#escargotCarre(T,400,100)

def escargotRond(T,size,steps):
    delta=size/steps
    while size > 0 :
        T.circle(size,90)
        size -= delta

#escargotRond(T,500,100)

################Exercice 3 :

def marche(T,direction,pas): #direction fournie par la fonction randomDir, égale à 0,90,-90.
    T.left(direction)
    T.forward(pas)

def marcheDroit(T,pas):
    marche(T,0,pas)
    marcheDroit(T,pas)

def randomDir():
    direction=rd.randint(-1,1)*90
    return(direction)

def marcheAleatoire(T,pas):
    marche(T,randomDir(),pas)
    marcheAleatoire(T,pas)

#fournit une liste de tortues de taille n  
def multiTurtle(n):
    L=n*[0]
    for i in range(n):
        L[i]=Turtle()
        L[i].color(randomColor())
        L[i].speed(0)
        L[i].shape('turtle')
    return(L)

def multiMarche(tortues,pas):
    for T in tortues:
        marche(T,randomDir(),pas)
    multiMarche(tortues,pas)

def randomColor():
    color='#'
    hexa='0123456789abcdef'
    for i in range(6):
        r=rd.randint(0,15)
        color += hexa[r]
    return(color)

""""""





#T.speed(1000)
delay(0)
#marcheAleatoire(T,10)
#multiMarche(multiTurtle(30),10)
#print(randomColor())


################Exercice 4 :


def randomPos(pas):
    borneLarge=1900//(2*pas) #nombre des cases contenues dans la demi largeur
    borneHaute=1000//(2*pas) #nombre des cases contenues dans la demi hauteur
    x=rd.randint(-borneLarge//3,borneHaute//3)*pas
    y=rd.randint(-borneHaute//3,borneHaute//3)*pas
    return([x,y])

def randomInit(pas,tortues,positions): #tortues et positions sont des listes
    n=len(tortues)
    for i in range(n):
        XY=randomPos(pas)
        tortues[i].penup()
        tortues[i].setpos(XY[0],XY[1])
        tortues[i].pendown()
        positions[i]=XY

def initialSize(pas,tortues):
    for T in tortues:
        T.turtlesize(pas//2,pas//2)

def multiMarcheTrack(pas,tortues,positions,distances):
    n=len(tortues)
    for i in range(n):
        marche(tortues[i],rd.randint(0,359),pas)
        positions[i]=tortues[i].pos()
    distances = updateDistance(distances,positions)
    murder(distances,tortues)

#####################La fonction à executer pour l'ancer l'auto Agar.io.
#####################La croissance est de x2 faire en sorte que ça se finisse facilement et que ce soit agréable à voir
#####################Grille de 5px avec 25 tortues est un bon équilibre
def agarAuto(pas,n):
    resizemode("user")
    tortues=multiTurtle(n)
    initialSize(pas,tortues)
    positions=n*[0]
    randomInit(pas,tortues,positions)
    distances = n*[0]
    for i in range(n):
        distances[i]=n*[0]
    while True :
        multiMarcheTrack(pas,tortues,positions,distances)

def updateDistance(distances,positions):
    n = len(positions)
    for i in range(n):
        for j in range(n):
            x1,x2,y1,y2 = positions[i][0],positions[j][0],positions[i][1],positions[j][1]
            distances[i][j] = sqrt((x1-x2)**2+(y1-y2)**2)
    return(distances)

def murder(distances,tortues):
    n=len(tortues)
    for i in range(n):
        size = tortues[i].turtlesize()[0]
        print(size)
        for j in range(n):
            if i!=j and distances[i][j] <= size*4 and tortues[i].xcor()<5000 :
                tortues[i].turtlesize(size*2,size*2)
                tortues[j].hideturtle()
                tortues[j].penup()
                tortues[j].setx(10000)
    #Un peu galérien, mais essentiellement j'envoie le tortues mangées en x=10000 et interdis aux tortues x>5000 de manger
    #A la fin, je supprime toutes les tortues avec x>5000 (donc les x=10000), et ça évite les problèmes d'indice.
    i=0
    while i<len(tortues):
        if tortues[i].xcor() > 5000 :
            del tortues[i]
        else:
            i += 1
    

agarAuto(5,25)


input('allez ça roule')
