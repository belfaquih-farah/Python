donnees = [
    ("Sara", "Math", 12, "G1"), ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"), ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"), ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"), ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"), ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3")
]
#Partie 1 : Nettoyage et validation des donnees
def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    
    if not nom or not matiere or not groupe:
        return False, "raison: nom/matière/groupe vide"
    try:
        note_float = float(note)
        if not (0 <= note_float <= 20):
            return False, "raison: note hors intervalle [0,20]"
    except (ValueError, TypeError):
        return False, "raison: note non numérique"
        
    return True, ""

valides = []
erreurs = []
doublons_exact = set()
deja_vus = []

for ligne in donnees:
    if ligne in deja_vus:
        doublons_exact.add(ligne)
    else:
        deja_vus.append(ligne)
        
    est_valide, message = valider(ligne)
    if est_valide:
        valides.append((ligne[0], ligne[1], float(ligne[2]), ligne[3]))
    else:
        erreurs.append({"ligne": ligne, "raison": message})

print(f"Lignes valides: {len(valides)}")

#Partie 2 : Structuration
matieres_distinctes = {ligne[1] for ligne in valides}
etudiants_notes = {}
for nom, matiere, note, groupe in valides:
    if nom not in etudiants_notes:
        etudiants_notes[nom] = {}
    if matiere not in etudiants_notes[nom]:
        etudiants_notes[nom][matiere] = []
    etudiants_notes[nom][matiere].append(note)

groupes = {}
for nom, matiere, note, groupe in valides:
    if groupe not in groupes:
        groupes[groupe] = set()
    groupes[groupe].add(nom)

#Partie 3 : Calculs et statistiques
def somme_recursive(liste):
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def calculer_moyenne(liste):
    if not liste:
        return 0
    return somme_recursive(liste) / len(liste)

for nom, matieres in etudiants_notes.items():
    toutes_les_notes = []
    print(f"\nÉtudiant: {nom}")
    for mat, notes in matieres.items():
        moy_mat = calculer_moyenne(notes)
        print(f"  - Moyenne en {mat}: {moy_mat}")
        toutes_les_notes.extend(notes)
    
    moy_generale = calculer_moyenne(toutes_les_notes)
    print(f"  > Moyenne Générale: {moy_generale:.2f}")   

#Partie 4 : Analyse avancée
alertes = []

for nom, matieres in etudiants_notes.items():
    for mat, notes in matieres.items():
        if len(notes) > 1:
            alertes.append(f"Alerte: {nom} a plusieurs notes en {mat}")

for nom, matieres in etudiants_notes.items():
    if len(matieres) < len(matieres_distinctes):
        alertes.append(f"Alerte: Profil incomplet pour {nom}")

for nom, matieres in etudiants_notes.items():
    toutes_notes = [n for list_n in matieres.values() for n in list_n]
    if max(toutes_notes) - min(toutes_notes) > 10:
        alertes.append(f"Alerte: Performance instable pour {nom} (écart > 10)")

print("\n--- Liste des alertes détectées ---")
for a in alertes:
    print(a)     