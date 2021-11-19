#cette exercice a pour but de de créer une fonction multiplication de matrice et de vérifier sa validitée ou non #

#bilbliothèques:#
import random as r

#Variables#
n=3
a=[]
b=[]
for i in range(n):
    a.append([r.randint(0,10) for i in range(n)])
    b.append( [r.randint(0,10) for i in range(n)])

def multiplication(i,j):
     #Cette fonction fait une multiplication (Antony.Guillot le 19/11/2021)#

    #variavles#
    nb_colonne_a=len(a[i])
    nb_ligne_b=len(b)
    S=0
    if nb_colonne_a==nb_ligne_b:
        for compteur in range(nb_colonne_a):
            S+=a[i][compteur]*b[compteur][j]
    else:
        print("le produit matritiel ne peut etre fait les dimensions ne corresponde pas")
    
    return S

def produit_matriciel(a,b):
    nb_ligne_a=len(a)
    nb_colonne_b=len(b[0])
    c=[]
    for compteur in range (nb_ligne_a):
        c.append([])
        for compteur2 in range (nb_colonne_b):
            c[compteur].append(multiplication(compteur,compteur2))
    return print(c)

produit_matriciel(a,b)