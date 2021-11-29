from turtle import*
from math import sqrt

T=Turtle()
T.penup()
T.goto(-700,0)
T.pendown()
T.speed(0)




def itérationVK(T,n,length):
    if n==0:
        T.forward(length)
    else :
        itérationVK(T,n-1,length/3)
        T.left(60)
        itérationVK(T,n-1,length/3)
        T.right(120)
        itérationVK(T,n-1,length/3)
        T.left(60)
        itérationVK(T,n-1,length/3)

#itérationVK(T,8,2000)



def itérationCrabe(T,n,length):
    if n==0:
        T.forward(length)
    else :
        T.left(45)
        itérationCrabe(T,n-1,length*(sqrt(2)/2))
        T.right(90)
        itérationCrabe(T,n-1,length*(sqrt(2)/2))
        T.left(45)

#itérationCrabe(T,9,500)


def itérationPeano(T,n,length):
    pas=length/3
    if n == 0 :
        T.forward(length)
    else :
        itérationPeano(T,n-1,pas)
        itérationPeano(T,n-1,pas)
        T.left(90)
        itérationPeano(T,n-1,pas)
        T.left(90)
        itérationPeano(T,n-1,pas)
        T.left(90)
        itérationPeano(T,n-1,pas)
        itérationPeano(T,n-1,pas)
        T.left(90)
        itérationPeano(T,n-1,pas)
        T.left(90)
        itérationPeano(T,n-1,pas)
        T.right(90)
        itérationPeano(T,n-1,pas)


#itérationPeano(T,5,1000)

def intérationSierpinski(T,n,length):
    pas = length/2
    if n == 0 :
        T.forward(length)
        T.left(120)
        T.forward(length)
        T.left(120)
        T.forward(length)
        T.left(120)
    else :
        intérationSierpinski(T,n-1,pas)
        T.forward(pas)
        intérationSierpinski(T,n-1,pas)
        T.forward(pas)
        T.left(120)
        T.forward(pas)
        intérationSierpinski(T,n-1,pas)


input("hop là qui va là?")