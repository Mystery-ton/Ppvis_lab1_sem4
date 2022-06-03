from Animal import Animal


class Omnivorous(Animal):
    __INITIAL_HUNGER_AMOUNT_OF_OMNIVOROUS: int = 10

    def __init__(self,type,food_priority,max_age,symbol):
        super().__init__()
        self.is_predator = True
        self.hunger = self.__INITIAL_HUNGER_AMOUNT_OF_OMNIVOROUS
        self.type = type
        self.food_priority = food_priority
        self.max_age = max_age
        self.symbol = symbol

    def clone(self, type: str, food_priority: int, max_age: int, symbol: str) -> "Animal":
        return super().clone(Omnivorous(type, food_priority, max_age, symbol))