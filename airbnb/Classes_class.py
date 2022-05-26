import unittest


class Player:

    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age


player1 = Player("Messi", 45)
print(player1.name)
print(player1.age)
