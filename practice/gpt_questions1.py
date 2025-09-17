"""
Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.

"""


# def fibonacci(n):
#     ls = [0, 1]

#     if n == 0:
#         return None
#     elif n == 1:
#         ls = [0]
#         return ls


#     for x in range(2,n):
#         print(x)
#         ls.append(ls[x-1] + ls[x-2])
#     return ls

# inp = int(input("How many fibonacci nums do you want to see?\n"))
# print(fibonacci(inp))

"""
Write a program that counts the number of vowels in a string.

"""

#ChatGPT help

# def v_count(s):
#     vowel = list("aeiouy")

#     m = map(s.count, vowel)
#     return sum(list(m))

#     # return s.count(vowel)

# inp = input("Count vowels in what word?\n")
# print(v_count(inp))


keys = ["a", "e", "i", "o", "u", "y"]
values = [1, 2, 3, 4, 5, 6]

vowels = dict(zip(keys, values))
print(vowels)