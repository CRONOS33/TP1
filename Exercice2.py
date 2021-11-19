#cette exercice a pour but de verifier la validitée d'un calandrier #

try:   
    valeur =int(input("entrer votre salaire annuelle"))
except ValueError:
        print(" toute les variable d'entrées sont de type Int")


def vos_impots(valeur):
    #Cette fonction propose de conpté vos impots (Antony.Guillot le 19/11/2021)#

    #variables#
    impots=0
    imposé=0
    if  valeur>=158123:
        imposé=valeur-158123
        valeur -=imposé
        impots += imposé*45/100
    elif  valeur>=73517:
        imposé=valeur-73517
        valeur -=imposé
        impots += imposé*41/100
    elif  valeur>=25711:
        imposé=valeur-25711
        valeur -=imposé
        impots += imposé*30/100
    elif  valeur>=10085:
        imposé=valeur-10085
        valeur -=imposé
        impots += imposé*10/100

    return print("vous allez payer "/impots/"d'impots" ) 


vos_impots(valeur)