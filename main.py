if __name__== '__main__':
    # Q1
    # Creation d'une liste  de 10 element  de type chaine de caracteres
    animaux = ["chameau", "chien", "lion", "oiseau", "poisson", "chevre", "vache", "cheval", "moustique", "canard"]
    
    # 1- Affichage des elements de la liste
    print("1) Affichage des elements de la liste")
    print("--------------------------------------------------")
    print(animaux)
    print("--------------------------------------------------\n")
    # 2- Changer le contenu de l'element numero 5
    print("2) Changement du contenu de l'element numero 5")
    print("--------------------------------------------------")
    animaux[4] = "requin"
    print(animaux)
    #3- Creation d'une nouvelle liste
    new_list = []
    # remplissage avec les elements de la liste precedente contenant la lettre "a"
    for element in animaux:
        if "a" in element:
            new_list.append(element)
    print("\n3) les elements de la liste contenant la letter a:")
    print("--------------------------------------------------")
    print(new_list)