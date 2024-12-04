from typing import Any


class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def take_damage(self, damage: int = 50) -> None:
        self.health -= damage
        if self.health <= 0:
            self.die()

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return f"[{", ".join(str(animal) for animal in cls.alive)}]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> Any:
        if not isinstance(other, Animal):
            raise TypeError("The object to bite "
                            "must be an instance of Animal.")
        if isinstance(other, Herbivore) and not other.hidden:
            other.take_damage(50)
