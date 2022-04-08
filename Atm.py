class Atm:
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def balance(self):
        print("Your balance is: $20")

    def withdrawal(self, amount):
        new_amount = 20-amount
        print("You have withdrawed: " + str(amount) + "Your balance is now:" + str(new_amount))

    def main():
        name = input("Please enter your name")
        print("Hello, " + name)
        cardnumber = input("Please enter your card number: ")
        pinnumber = input("Please enter your pin number: ")
        new_user = Atm(cardnumber, pinnumber)

        print("Hello" + name + "! Choose your activity")
        print("1. Balance")
        print("2. Withdrawal")
        activity = int(input("Enter your activity choice"))

        if (activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int(input("Enter amount:"))
            new_user.cashwidthdrawal(amount)
        else:
            print("Enter a valid number")

if __name__ == "__main__":
    main()