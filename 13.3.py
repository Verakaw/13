from pydoc import describe

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        print(self.rating)
    def open_restaurant(self):
        print(self.restaurant_name, " открыт!!")
    def update_rating(self):
        print(self.rating)
newRestaurant = Restaurant("Сударыня", "русская", 4.8)
newRestaurant.describe_restaurant()