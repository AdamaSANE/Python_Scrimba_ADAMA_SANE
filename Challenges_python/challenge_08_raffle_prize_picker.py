# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.

# Demander le nombre de participants au tirage au sort
num_people = int(input("How many people are entering the raffle? "))

# Vérifier qu'il y a au moins 3 participants
if num_people < 3:
  print("You need at least 3 participants to run the raffle!")
  exit()

# Créer une liste vide pour stocker les noms des participants
participants = []

# Collecter les noms de tous les participants via une boucle
for i in range(num_people):
  name = input(f"Enter name #{i+1}: ")
  participants.append(name)  # Ajouter chaque nom à la liste  # Ajouter chaque nom à la liste

# Créer une liste vide pour stocker les 3 prix
prizes = []

# Collecter les noms des 3 prix (le dernier sera le Grand Prix)
for i in range(3):
  prize = input(f"Prize #{i+1}: ")
  prizes.append(prize)  # Ajouter chaque prix à la liste  # Ajouter chaque prix à la liste

# Importer le module random pour sélectionner des gagnants aléatoires
import random

# Sélectionner 3 gagnants différents de manière aléatoire (sans répétition)
winners = random.sample(participants, 3)

# Afficher l'en-tête des résultats du tirage au sort
print("===== 🎉 Raffle Results 🎉 =====")

# Parcourir les 3 gagnants et afficher qui remporte quel prix
for i in range(3):
  if i == 2:  # Le dernier gagnant (index 2) remporte le Grand Prix
    print(f"\n🏆 GRAND PRIZE: {winners[i]} wins the {prizes[i]}!")
  else:  # Les deux premiers gagnants remportent des prix réguliers
    print(f" - {winners[i]} wins the {prizes[i]}")

# Afficher le pied de page
print("===============================")