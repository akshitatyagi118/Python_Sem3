class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.category = self.categorize()

    def categorize(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print("Mobile added successfully!")

    def display_all(self):
        if not self.mobiles:
            print("No mobiles available in the store.")
        else:
            print("\n===== Mobile Store =====")
            for mobile in self.mobiles:
                mobile.display()


# Create Store object
store = Store()

# Add mobiles
mobile1 = Mobile("Apple", "iPhone 15", 65000)
mobile2 = Mobile("Samsung", "Galaxy A55", 35000)
mobile3 = Mobile("Redmi", "Note 13", 15000)

store.add_mobile(mobile1)
store.add_mobile(mobile2)
store.add_mobile(mobile3)

# Display all mobiles
store.display_all()


# OUTPUT:

# Mobile added successfully!
# Mobile added successfully!
# Mobile added successfully!
#
# ===== Mobile Store =====
# Brand: Apple
# Model: iPhone 15
# Price: ₹65000
# Category: Premium
# ------------------------------
# Brand: Samsung
# Model: Galaxy A55
# Price: ₹35000
# Category: Mid-range
# ------------------------------
# Brand: Redmi
# Model: Note 13
# Price: ₹15000
# Category: Budget
# ------------------------------