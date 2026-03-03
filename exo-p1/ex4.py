nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

print("\n--- CHOISISSEZ UNE OPÉRATION ---")
print("1 : addition")
print("2 : soustraction")
print("3 : multiplication")
print("4 : division")

choix = input("Votre choix (1, 2, 3 ou 4) : ")

if choix == "1":
    resultat = nombre1 + nombre2
    print(f"Résultat de l'addition : {resultat}")

elif choix == "2":
    resultat = nombre1 - nombre2
    print(f"Résultat de la soustraction : {resultat}")

elif choix == "3":
    resultat = nombre1 * nombre2
    print(f"Résultat de la multiplication : {resultat}")

elif choix == "4":
    if nombre2 == 0:
        print("Erreur : Impossible de diviser par zéro !")
    else:
        resultat = nombre1 / nombre2
        print(f"Résultat de la division : {resultat}")

else:
    print("Choix invalide. Veuillez relancer le programme et choisir entre 1 et 4.")