from typing import override
from spaceship_decorator import SpaceshipDecorator
from ispaceship import ISpaceship


class ShieldDecorator(SpaceshipDecorator):
    def __init__(self, spaceship: ISpaceship, shield_name: str = "Standard Shield", extra_defense: int = 10,
                 extra_weight: int = 20):
        super().__init__(spaceship)
        self.shield_name = shield_name
        self.extra_defense = extra_defense
        self.extra_weight = extra_weight

    @override
    def get_defense(self) -> int:
        return self._spaceship.get_defense() + self.extra_defense

    @override
    def get_weight(self) -> int:
        return self._spaceship.get_weight() + self.extra_weight

    @override
    def get_details(self) -> str:
        return f"{self._spaceship.get_details()}, {self.shield_name}"
