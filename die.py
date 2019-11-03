from random import randint
class Die():
    
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, 6)
        print(x)


if __name__ == '__main__':
    die1 = Die()
    die1.roll_die()
