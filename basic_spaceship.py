from ispaceship import ISpaceship
from typing import override


class BasicSpaceship(ISpaceship):
    def __init__(self):
        self._attack = 10
        self._defense = 50
        self._weight = 100

    @override
    def get_attack(self) -> int:
        return self._attack

    @override
    def get_defense(self) -> int:
        return self._defense

    @override
    def get_weight(self) -> int:
        return self._weight

    @override
    def get_details(self) -> str:
        return "BasicSpaceship"

    def __str__(self) -> str:
        return (f"{self.get_details()} "
                f"[Attack: {self.get_attack()}, "
                f"Defense: {self.get_defense()}, "
                f"Weight: {self.get_weight()}]")
