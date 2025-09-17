import string

# def str2dict(s):
#     letter_count = {}
#     count = 0
#     for letter in s:
#         for x in s:
#             if x == letter:
#                 count+=1
#         letter_count[f"{letter}"] = count
#         count = 0

    
#     return letter_count

def str2dict_plus(s):
    letter_count = {}
    count = 0
    for letter in s:
        if letter != " " and letter not in string.punctuation:
            for x in s:
                if x == letter:
                    count+=1
            letter_count[f"{letter}"] = count
            count = 0

    
    return letter_count

# print(str2dict("Hello World"))
print(str2dict_plus("Hello World !!!"))

