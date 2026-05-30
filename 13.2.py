from pydoc import describe

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name, " открыт!!")
Restaurant2 = Restaurant("Casa Mexico", "мексиканская")
Restaurant3 = Restaurant("Золотой Дракон", "азитская")
Restaurant4 = Restaurant("Сударыня", "русская")
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()
Restaurant4.describe_restaurant()