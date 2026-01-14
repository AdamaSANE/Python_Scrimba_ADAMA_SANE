# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."


# Demande à l'utilisateur de saisir un numéro de téléphone US dans n'importe quel format
print("\n=== Phone Number Formatter ===")
phone_input = input("Enter a U.S. phone number (any format): ")


# Supprime les espaces en début et fin de chaîne
cleaned = phone_input.strip()


# Remplace les séparateurs courants par des espaces
for ch in ["-", "(", ")", "."]:
    cleaned = cleaned.replace(ch, " ")
    

# Découpe la chaîne en morceaux, puis fusionne tous les chiffres
parts = cleaned.split()
digits_only = "".join(parts)


# Vérifie si le numéro contient exactement 10 chiffres
if len(digits_only) == 10:
    # Sépare les différentes parties du numéro
    area = digits_only[0:3]
    mid = digits_only[3:6]
    end = digits_only[6:]
    # Affiche le numéro formaté standard US
    print(f"Formatted number: ({area}) {mid}-{end}")
else:
    # Affiche un message d'erreur si le format n'est pas respecté
    print("Error: Please enter exactly 10 digits.")
    
print("===========================")
# ✅ Test it out!
#
#  - 123-456-7890
#  - (123)4567890
#  - 123. 456 . 7890
#  -    123 456 7890   
#  - 1234567890
#  - 123-45-789
#  - abc-456-7890
#  - 12345678901234