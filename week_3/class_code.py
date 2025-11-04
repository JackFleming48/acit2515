myl = [1,4,5,7,4,56,3]

myl = sorted(myl)

print(myl)

with open("names.txt", "r") as f:
    data = f.read()

print(f"data from names.txt:\n {data}")

# with open("refact.txt", "w") as f:
#     f.write(data)

a, b = ['this', 'test']
print("using a list and assigning the list => a, b = ['this', 'test']")
print(a)
print(b)

a = b = c = "bob"

print("a = b = c = 'bob'")
print(a,b,c)