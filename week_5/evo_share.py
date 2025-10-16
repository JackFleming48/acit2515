class Evo:
    
    def __init__(self):
        self.driver = None
        self.distance = 0
        self.in_use = False

    def start_rental(self, driver_name):
        if self.driver != None:
            raise RuntimeError("Car is in use!")
        self.driver = driver_name
        self.in_use = True

    def drive(self, driven):
        if driven < 0:
            raise AttributeError("Driven distance cannot be 0")
        elif self.driver == None:
            raise  RuntimeError("There must be a driver")
        self.distance += driven


    def end_rental(self):
        if not self.in_use:
            raise RuntimeError("There must be a driver")
        self.in_use = False
        self.driver = None
        return self.distance
    
def main():
    car = Evo()
    car.start_rental("khabib")
    car.drive(105)
    car.drive(15)
    total = car.end_rental()
    print(f"its going to cost you ${float(total)}")

if __name__ == "__main__":
    main()