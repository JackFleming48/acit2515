def count_people(filename):
    with open(filename, "r") as fp:
        return len(fp.readlines())
    
    #Returns the length of the list


