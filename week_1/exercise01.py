def str2dict(s):
    letter_count = {}
    count = 0
    for letter in s:
        for x in s:
            if x == letter:
                count+=1
        letter_count[f"{letter}"] = count
        count = 0

    
    return letter_count

print(str2dict("Hello"))