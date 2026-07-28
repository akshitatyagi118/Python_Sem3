from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ${amount} processed using Credit Card.")


# Strategy 2
class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs {amount} processed using Debit Card.")


# Strategy 3
class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs {amount} processed using UPI.")


# Strategy 4
class NetBankingPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs {amount} processed using Net Banking.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


# Driver Code
processor = PaymentProcessor()

while True:
    print("\n===== Payment Processing System =====")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you for using the Payment System!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice!")
            continue

        amount = float(input("Enter payment amount: "))

        if choice == 1:
            processor.set_strategy(CreditCardPayment())
        elif choice == 2:
            processor.set_strategy(DebitCardPayment())
        elif choice == 3:
            processor.set_strategy(UpiPayment())
        elif choice == 4:
            processor.set_strategy(NetBankingPayment())

        processor.process_payment(amount)

    except ValueError:
        print("Please enter valid numeric input.")



# ---------------- SAMPLE OUTPUT ----------------
#
# ===== Payment Processing System =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 1
# Enter payment amount: 500
# Payment of $500.0 processed using Credit Card.
#
# ===== Payment Processing System =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 3
# Enter payment amount: 1200
# Payment of $1200.0 processed using UPI.
#
# ===== Payment Processing System =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 4
# Enter payment amount: 850
# Payment of $850.0 processed using Net Banking.
#
# ===== Payment Processing System =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 5
# Thank you for using the Payment System!