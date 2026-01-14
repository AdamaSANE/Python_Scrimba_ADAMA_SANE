# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"


# Collecte des entrées utilisateur
total_race_time = float(input("Enter total race time (in seconds): "))  # Temps total de la course
num_pit_stops = int(input("Enter number of pit stops: "))              # Nombre d'arrêts au stand
avg_pit_duration = float(input("Enter average pit stop duration (in seconds): "))  # Durée moyenne d'un arrêt


# Calcule le temps total passé aux stands
total_pit_time = num_pit_stops * avg_pit_duration


# Calcule le pourcentage du temps de course passé aux stands
pit_percentage = (total_pit_time / total_race_time) * 100
pit_percentage = round(pit_percentage, 2)


# Affiche le résumé des arrêts au stand
print("\n=== Pit Stop Summary ===")
print(f"Total pit stop time: {total_pit_time} seconds")
print(f"Percentage of race in pits: {pit_percentage}%")


# Message d'avertissement si le temps aux stands dépasse 5%
if pit_percentage > 5:
    print("You need a new pit crew. 🛠️")
print("=========================")