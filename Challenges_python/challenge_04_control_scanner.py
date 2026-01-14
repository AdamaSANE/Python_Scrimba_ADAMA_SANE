# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.


 # Ensemble des numéros de badges révoqués
revoked_badges = {"X123", "B789", "Z999"}

denied = []

# Listes pour stocker les visiteurs approuvés et refusés
approved = []
denied = []


# Boucle principale pour collecter les informations des visiteurs
while True:
    # Demande le nom du visiteur
    name = input("Enter person's name (or type 'done' to finish): ")
    if name.lower() == "done":
        break

    # Demande le numéro de badge et le formate
    badge = input("Enter badge number: ").strip().upper()

    # Vérifie si le badge est révoqué
    if badge in revoked_badges:
        denied.append(name)
        print(f"[ACCESS DENIED] {name} - Revoked badge")
    else:
        approved.append(name)
        print(f"[ACCESS GRANTED] {name}")


# Affichage du résumé d'accès
print("===== Access Summary =====")


# Affiche la liste des visiteurs approuvés, triée par ordre alphabétique
print("✅ Approved Visitors:")
for person in sorted(approved):
    print(f" - {person}")


# Affiche la liste des visiteurs refusés, triée par ordre alphabétique
print("⛔️ Denied Visitors:")
for person in sorted(denied):
    print(f" - {person}")


# Affiche le total des visiteurs approuvés et refusés
print(f"Total Approved: {len(approved)}")
print(f"Total Denied: {len(denied)}")
print("===========================")