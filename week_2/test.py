# from week2_lecture import str2dict

# str2dict("hello world

with open("test.txt", "r") as f:
    data = f.read()
    d = data.split()

with open("test.txt", "w") as f:
    count = 1
    for x in d:
        f.write(f"{count} {x}\n")
        count+=1

 