from math import*
import random as rd

def rList(n):
    L=n*[0]
    for i in range(n):
        L[i]=rd.randint(0,10000)
    return(L)

def selectionSort(L):
    n = len(L)
    res = n*[0]
    for i in range(n):
        m=min(L)
        res[i]=m
        L.remove(m)
        print(res)
        print(L)
    return(res)

def merge(L1,L2):
    n=len(L1)+len(L2)
    L=n*[0]
    top=max(L1)**2+max(L2)**2 #plus grand que tous les autres, sert à éviter d'avoir une liste vide et donc un index out of range
    L1.append(top)
    L2.append(top)
    for i in range(n):
        L[i]=min(L1[0],L2[0])
        if L1[0]<L2[0]:
            del L1[0]
        else:
            del L2[0]
    print(L)
    return(L)

def mergesort(L):
    n=len(L)
    if n==1:
        return(L)
    else:
        s=floor(n/2)
        L1=L[:s]
        print(L1) #cosmétique
        L2=L[s:]
        print(L2) #cosmétique
        L1=mergesort(L1)
        L2=mergesort(L2)
        return(merge(L1,L2))


#L=rList(1000)
#L=selectionSort(L)


L=rList(10000000)
L=mergesort(L)

input('pour pas fermer la fenêtre exécutable directement')