class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients  # ingredient: quantity

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += quantity * ingredient_price
                return
            self.ingredients[ingredient] = quantity
            self.price += quantity * ingredient_price
            return
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price
            return
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def pizza_ordered(self):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join(f'{x}: {str(y)}' for x, y in self.ingredients.items())}" \
               f" and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))
