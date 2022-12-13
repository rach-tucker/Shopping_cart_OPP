### Exercise 1 - Turn the shopping cart program into an object-oriented program

class Cart():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.list = {}
        self.total = []


    def add_to_cart(self):
        item = input("What would you like to add?")
        quantity = input(f"How many {item}'s do you want to add?")
        cost = float(input(f"How much does a {item} cost?"))
        final_cost  = (float(cost) * int(quantity))
        self.total.append(final_cost)
        self.list[item] = (int(quantity), cost)
        if int(quantity) > 1:
            print(f"{quantity} {item}'s have been added to your cart.")
        if int(quantity) == 1:
            print(f"{quantity} {item} has been added to your cart.")

    def remove_from_cart(self):
        remove = input("What item do you want to remove?")
        remove_quantity = input(f"How many {remove}'s do you want to remove?")
        self.list[remove] = (self.list[remove][0] - int(remove_quantity), self.list[remove][1])
        if int(quantity) > 1:
            print(f"{quantity} {item}'s have been removed to your cart.")
        if int(quantity) == 1:
            print(f"{quantity} {item} has been removed to your cart.")

    def show_cart(self):
        print("Here is your shopping cart:")
        for item, (quantity,cost) in self.list.items():
            print(f"{quantity} {item} x ${cost}")

    def clear_cart(self):
        check = input("Are you sure you want to clear your shopping cart? This action cannot be undone. (Y/N)")
        if check == "Y":
            self.list.clear()
            print("Your shopping cart has been emptied.")

    def quit(self):
        quit = input("Are you sure you want to quit? (Y/N)")
        if quit == "Y":
            print("Here is your shopping cart receipt:")
            for item, (quantity,cost) in self.list.items():
                print(f"{quantity} {item} x ${cost}")
            print(f"Your total is " "$" + str(round(sum(total),2)))

    def run(self):
        while True:
            ask = input("What would you like to do? (Add/Remove/Show/Clear/Quit)").title()
            if ask == 'Add':
                self.add_to_cart()
            elif ask == "Remove":
                self.renove_from_cart()
            elif ask == "Show":
                self.show_cart()
            elif ask == "Clear":
                self.clear_cart()
            elif ask == "Quit":
                self.quit()
                break
            else:
                print("invalid entry, please try again.") 

my_cart = Cart('Rachel')


my_cart.run
           
    