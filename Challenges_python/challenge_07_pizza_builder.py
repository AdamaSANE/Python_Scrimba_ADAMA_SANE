#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary
class Pizza:
    def __init__(self, size, crust_type, toppings=None):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings if toppings else []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"✅ Added {topping}")
    
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f"❌ Removed {topping}")
        else:
            print(f"⚠️ {topping} not found on this pizza")
    
    def print_details(self):
        print("\n=== 🍕 Pizza Details ===")
        print(f"Size: {self.size}")
        print(f"Crust: {self.crust_type}")
        if self.toppings:
            print(f"Toppings: {', '.join(self.toppings)}")
        else:
            print("Toppings: No toppings yet!")

# Create and customize a pizza
print("\n=== 🍕 Welcome to the Pizza Builder Challenge! 🍕 ===")
my_pizza = Pizza("Large", "Thin crust")
my_pizza.add_topping("Pepperoni")
my_pizza.add_topping("Mushrooms")
my_pizza.add_topping("Extra cheese")
my_pizza.remove_topping("Mushrooms")
my_pizza.remove_topping("Olives")  # Not on the pizza
my_pizza.print_details()

print("\n=== 🍕 Enjoy your custom pizza! 🍕 ===")