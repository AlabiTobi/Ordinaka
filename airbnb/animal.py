class Animal:
    def _init_(self, name: str, age=0) -> None:
        self.name = name

    def speak(self):
        return "I speak "


class Dog(Animal):
    def _init(self, type, age, name: str):
        super()._init_(name, age)
        self.age = 0
        self.type = type

    def speaking(self):
        return "like a "


class Cat(Animal):
    pass


dog = Dog("Bingo", 0, "local dog")
print(f'{dog.speak()}{dog.speaking()}{dog.type}')
cat = Cat("Kitten")
print(cat.speak())
print(dog.name)
print(dog.age)


# Inheriting from different classes
class Bingo(Dog, Animal):
    pass


bingo = Bingo("bingo", 0, "local")
help(bingo)
