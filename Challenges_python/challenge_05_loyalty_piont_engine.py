# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier


# Historique des achats (exemples de montants)
purchases = [12.50, 34.20, 299.99]

def earn_points(price):
    """
    Convertit un montant d'achat en points (3 points par dollar entier).
    Les fractions de dollar ne comptent pas.
    """
    whole_dollar = int(price)  # Prend uniquement la partie entière du montant
    return whole_dollar * 3
    
def tier_label(points):
    """
    Retourne le nom du palier de fidélité selon le total de points.
    """
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"

# Initialisation des totaux
total_spent = 0.0  # Total dépensé
total_points = 0   # Total de points cumulés

# Parcours de chaque achat pour calculer les points et le total dépensé
for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

# Détermination du palier final atteint
final_tier = tier_label(total_points)

# Affichage du résumé de fidélité
print("===== Loyalty Summary =====")
print(f"Total spent: ${total_spent:.2f}")
print(f"Total points: {total_points}")
print(f"Tier achieved: {final_tier}")
print("===========================")