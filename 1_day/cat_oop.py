class Cat:
    # Class Atributes
    species = 'mammel'
    legs = 4
    eyes = 2
    tail = 1 
    evil = True

    # 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def eat(self, food):
        return f"{self.name} ate {food}"

nell = Cat('Nell', 4)

print(nell)
print(nell.description())
print(nell.eat('fish'))
