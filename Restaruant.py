# -*- coding='utf-8' -*-
class Restaruant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def discribe_restaurant(self):
        print('restaurant name is {0}.'.format(self.restaurant_name))
        print('restaurant type is {0}.'.format(self.cuisine_type))

    def open_restaurant(self):
        print('{} opening!'.format(self.restaurant_name))

    def read_number_served(self):
        print("There has {0} peoples".format(self.number_served))

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number1):
        self.number_served += number1


if __name__ == '__main__':
    restaurant = Restaruant('qiaojiangnan', 'zhongcan')
    restaurant.set_number_served('20')
    restaurant.read_number_served()
    restaurant.increment_number_served('5')
    restaurant.read_number_served()
