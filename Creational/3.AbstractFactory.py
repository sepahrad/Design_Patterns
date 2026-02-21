from abc import ABC, abstractmethod

class FoodType:
    american = 1
    french = 2
    italian = 3

class Restaurant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass

class AmericanRestaurant(Restaurant):
    def make_food(self):
        return "Making a burger"

    def make_drink(self):
        return "Making a soda"

class FrenchRestaurant(Restaurant):
    def make_food(self):
        return "Making a croissant"

    def make_drink(self):
        return "Making a glass of wine"

class RestaurantFactory:
    @staticmethod
    def get_restaurant(food_type):
        restaurants = {
            FoodType.american: AmericanRestaurant,
            FoodType.french: FrenchRestaurant
        }
        
        restaurant_class = restaurants.get(food_type)

        if restaurant_class:
            return restaurant_class()
        
        raise ValueError(f"Unknown food type: {food_type}")

def dine_out(food_type: FoodType):
    restaurant = RestaurantFactory.get_restaurant(food_type)
    print(restaurant.make_food())
    print(restaurant.make_drink())

# Client code
if __name__ == "__main__":
    dine_out(FoodType.american)
    dine_out(FoodType.french)


