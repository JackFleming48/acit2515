
class Microwave:
    # initializers = __init__ 
    # dunder method
    # this takes care of initializing the class
    # it is ran when we obstantiate
    def __init__(self, brand, power_rating): # self refers to whatever instance you are using
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:
            print(f'Microwave {self.brand} is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is now turned on.')
            
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is already turned off.')

    def run(self, seconds):
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else:
            print('Already running')

    def __add__(self, other):
        return f'{self.brand} + {other.brand}'
    
    def __str__(self):
        return f'{self.brand} (Rating: {self.power_rating})'
    
smeg = Microwave('smeg','B') # Creating an instance of this class. Can also do smeg: Microwave = Microwave() to type annotate
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(30)
# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

bosch = Microwave('bosch', 'A') # Another instance
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)

print(smeg + bosch)
print(smeg)
print(bosch)