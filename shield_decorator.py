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
    def defense_get(self) -> int:
        return self._spaceship.defense_get() + self.extra_defense

    @override
    def weight_get(self) -> int:
        return self._spaceship.weight_get() + self.extra_weight

    @override
    def details_get(self) -> str:
        return f"{self._spaceship.details_get()}, {self.shield_name}"
