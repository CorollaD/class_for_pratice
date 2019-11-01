# -*- coding:utf-8 -*-
class Dog():

    def __init__(self, name, age):
        # """initialized belongs of name and age"""
        self.name = name
        self.age = age

    def sit(self):
        #""" mimic dog's sit """
        print("{0} is now sitting.".format(self.name.title()))

    def roll_over(self):
        #""" mimic dog's roll over """
        print("{0} rolled over!".format(self.name.title()))


if __name__ == '__main__':
    my_dog = Dog('willia', 6)
    print("My dog is {0}.".format(my_dog.name.title()))
    print("My dog is {0} years old.".format(str(my_dog.age)))
    print(my_dog.name.title())
    my_dog.sit()
    my_dog.roll_over()
    print('---------')
    your_dog = Dog('lucy', 3)
    print("\nYour dog's name is {0}.".format(your_dog.name.title()))
    print("Your dog is {0} years old.".format(str(your_dog.age)))
    your_dog.sit()

