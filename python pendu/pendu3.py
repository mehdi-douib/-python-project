import random
mots = [] 
with open ("dico_france.txt") as read_file: 
    for line in read_file: 
        mots.append(line.rstrip("\n")) 
mot = random.choice(mots)
# déclaration des variables
lettres = [] 
faux = 0 
trouvé = False 
niveau=[]
while niveau != 1 and niveau != 2 and niveau != 3:
    niveau = int(input ("!\nChoisissez un niveau :\n1 = Debutant / 2 = Intermediaire / 3 = Expert\n-->"))

    if niveau == 1:
        vies = 10
    elif niveau == 2:
        vies = 6
    elif niveau == 3:
        vies = 3
    else:
        print("choisir un niveau")
while not trouvé: 
    trouvé = True 
    nb_vies_depart = vies
    vies_restantes = nb_vies_depart - faux
    for la_lettre in mot: 
        if la_lettre in lettres: 
            print(la_lettre, end=" ") 
        else: 
            trouvé = False 
            print("_", end=" ") 
    print() 
    print("Nombre de vies : " , vies_restantes)
    print("Lettres proposées : ", end="") 
    for la_lettre in lettres: 
        print(la_lettre, end=" | ") 
    if faux >= nb_vies_depart: 
        print()
        print("tu a Perdu !") 
        print("Le mot était : {}".format(mot))
        break 
    if trouvé: 
        print()
        print("Tu as gagné!")
        break 
    print() 
    lettre = input("")
    lettres.append(lettre)
    if lettre not in mot:
        faux += 1 