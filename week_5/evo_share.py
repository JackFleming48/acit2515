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


    def drive(self):
        pass

    def end_rental(self):
        pass
