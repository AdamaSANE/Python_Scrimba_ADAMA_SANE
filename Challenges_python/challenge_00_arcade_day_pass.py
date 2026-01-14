# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available


# Déclaration des variables principales
customer_name = "Guil"           # Nom du client
passes_bought = 5                 # Nombre de pass achetés
tokens_per_pass = 30              # Jetons par pass
pass_price = 12.50                # Prix d'un pass
tokens_per_game = 4               # Jetons nécessaires par partie


# Calculs des totaux
total_tokens = passes_bought * tokens_per_pass      # Total de jetons obtenus
total_cost = passes_bought * pass_price             # Coût total
games_available = total_tokens // tokens_per_game   # Nombre de parties possibles (division entière)


# Affichage du résumé pour le client
print("===== ARCADE DAY PASS =====")
print("Customer:", customer_name)
print("Passes:", passes_bought)
print("Tokens:", total_tokens)
print(f"Total Cost: ${total_cost:.2f}")
print("Games Available: " + str(games_available))
print("===========================")