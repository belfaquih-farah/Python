saisie = input("Veuillez entrer votre age : ")

age = int(saisie)

if age < 0:
    message = "Âge non valide."
elif age <= 12:
    message = "Vous êtes un Enfant."
elif age <= 17:
    message = "Vous êtes un Adolescent."
elif age <= 64:
    message = "Vous êtes un Adulte."
else:
    message = "Vous êtes un Senior."

print(message)