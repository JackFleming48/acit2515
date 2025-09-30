'''
Class -> tv model SQ500

Methods -> tuner, pcb,  
Attribute -> On or Off, Channel
Object -> S/N


'''
class StatString:

    def __init__(self, input_string=""):
        self.raw_data = input_string
        # self.letters = clean_chars(input_string)

    def get_data(self):
        return self.raw_data
    
    def get_letters(self):
        return self.letters

    def set_data(self, input_string):
        self.__init__(input_string)


def main():
    """Demonstrate usage of StatString class"""

    #Create an instance of StatString
    stat_string = StatString("This is a test")
    print(stat_string)

if __name__ == "__main__":
    main()