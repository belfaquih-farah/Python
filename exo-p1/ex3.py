secret = "python123"

saisie = input("Entrez le mot de passe : ")

while saisie != secret:
    print("Mot de passe incorrect. Essayez encore.")
    saisie = input("Entrez le mot de passe : ")

print("Mot de passe correct ! Confirmation : Accès autorisé.")