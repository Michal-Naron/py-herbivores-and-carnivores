class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append({
                "Name": self.name,
                "Health": self.health,
                "Hidden": self.hidden,
            })

    def check_is_alive(self) -> None:
        if self.health <= 0:
            Animal.alive = [i for i in Animal.alive if i["Name"] != self.name]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            herbivore.check_is_alive()
