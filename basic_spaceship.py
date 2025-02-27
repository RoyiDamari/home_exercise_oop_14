from ispaceship import ISpaceship
from typing import override


class BasicSpaceship(ISpaceship):
    def __init__(self):
        self._attack = 10
        self._defense = 50
        self._weight = 100

    @override
    def attack_get(self) -> int:
        return self._attack

    @override
    def defense_get(self) -> int:
        return self._defense

    @override
    def weight_get(self) -> int:
        return self._weight

    @override
    def details_get(self) -> str:
        return "BasicSpaceship"

    def __str__(self) -> str:
        return (f"{self.details_get()} "
                f"[Attack: {self.attack_get()}, "
                f"Defense: {self.defense_get()}, "
                f"Weight: {self.weight_get()}]")
