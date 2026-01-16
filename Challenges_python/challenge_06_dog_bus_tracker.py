# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times. 

MAX_SEATS = 8

bus = {
  1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
  2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
  3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
}

print("-- Starting roster --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")

if len(bus) < MAX_SEATS:
  seat_num = len(bus) + 1
  new_pet = {
    "name": "Sir Barks-a-Lot",
    "breed": "Corgi Knight",
    "pickup": "8:45 AM",
    "dropoff": "4:45 PM",
  }
  bus[seat_num] = new_pet
  print(f"\n👋  {new_pet['name']} boards (seat {seat_num}).")
else:
  print("\n🚫  No free seats.")

print("\n-- Roster after pickup --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']}")


remove_name = input("\nWho goes home early? ").strip().lower()

seat_to_remove = 0
for seat, info in bus.items():
  if info['name'].lower() == remove_name:
    seat_to_remove = seat
    break

if seat_to_remove:
  gone = bus.pop(seat_to_remove)
  print(f"\n👋  {gone['name']} (seat {seat_to_remove}) heads home early.")
else:
  print(f"\n⚠️  No passenger name '{remove_name}' on the bus.")


print("\n-- Final roster --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff']})")
print("\n🐾  All pets have been dropped off. Goodbye!")
print("----------------------")

