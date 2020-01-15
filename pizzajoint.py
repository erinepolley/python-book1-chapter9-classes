class Pizza:
    def __init__(self, name, crust):
        self.name = name
        self.crust = crust
        # self.topping = ""
        self.cost = 10
        self.toppings = []
    def add_topping(self, topping):
        self.toppings.append(topping)
    def print_order(self):
        print(f"I would like the {self.name} pizza please, with the {self.crust} crust and the {self.toppings} toppings. Does it still cost {self.cost} dollars?")


# meat_lovers = Pizza("cheese", "thin")
# meat_lovers.add_topping("Olives")

# print(meat_lovers.toppings)

vegetarian_lovers = Pizza("peppers", "hand-tossed")

vegetarian_lovers.print_order()

