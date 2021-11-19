#cette exercice a pour but de de créer une date et de vérifier sa validitée ou non #

def bissextile (année):
    #   Cette fonction vérifie si une annnée est bissextile ou non (Antony.Guillot le 19/11/2021)#
    return année%400 == 0 or (année%100!=0 and année%4==0)


def jour_mois (numero_mois,année):
    #   Cette fonction donne le jour d'un certain moi d'une certaine année (Antony.Guillot le 19/11/2021)#

    #variable#
    nb_jour=0
    mois_nb31=[1,3,5,7,8,10,12]
    mois_nb30=[4,6,9,11]

 
    try:
        int(année)
        int(numero_mois)
    except ValueError:
        print("Toute les variable d'entrées sont de type Int")

    if numero_mois<1 and numero_mois>12 :
        return print("ils faut rentrer un numero de mois (inferieur a 12 et supérieur à 0) ")

    elif numero_mois in mois_nb31:
        nb_jour=31

    elif numero_mois in mois_nb30:
        nb_jour=30

    elif numero_mois==2 and bissextile(année):
        nb_jour=29

    else:
        nb_jour=28

    return     nb_jour



def valide_date(numero_jour,numero_mois,année):
     #   Cette fonction vérifie si une date est valide ou non (Antony.Guillot le 19/11/2021)#
    
    try:
        int(numero_jour)
        int(année)
        int(numero_mois)
    except ValueError:
        print(" toute les variable d'entrées sont de type Int")

    return numero_jour <= jour_mois(numero_mois,année) and numero_jour >= 1 


def creation_date():
    #Cette fonction propose la creation d'une date et sa vérification (Antony.Guillot le 19/11/2021)#

    #entré des donnée de la date#
    try:
        numero_jour = int(input ("entré le numero du jour   "))
        
        numero_mois = int(input("entré le numero du mois    "))
        numero_année = int(input("entré le numero de l'année    "))
    except ValueError:
        print(" toute les variable d'entrées sont de type Int")


    if valide_date(numero_jour,numero_mois,numero_année ):
        return print("la date est valide")
    else:
        return print("la date n'est pas valide") 


creation_date()
