contacts = ["Bouchra", "Ahmed", "Sara"]

continuer = True

while continuer:
    print("\n--- MENU CARNET D'ADRESSES ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter")
    
    choix = input("Votre choix : ")

    if choix == "1":
        nouveau = input("Nom du contact à ajouter : ")
        contacts.append(nouveau)
        print(f"{nouveau} a été ajouté.")

    elif choix == "2":
        print("\nListe des contacts numérotés :")
        for index, nom in enumerate(contacts, 1):
            print(f"{index}. {nom}")

    elif choix == "3":
        print("Fin du programme.")
        continuer = False
    
    else:
        print("Choix non valide.")