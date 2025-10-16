class Dog:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

rocky = Dog("rocky")
print(rocky.name)
cooper = Dog("cooper", 7)
print(cooper.age, cooper.name)

class Counter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def increment(self):
        self.value += self.step

c = Counter(2)

c.increment()
c.increment()
print(c.value)