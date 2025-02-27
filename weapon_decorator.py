from typing import override
from spaceship_decorator import SpaceshipDecorator
from ispaceship import ISpaceship


class WeaponDecorator(SpaceshipDecorator):
    def __init__(self, spaceship: ISpaceship, weapon_name: str = "Laser Rifle", extra_attack: int = 15,
                 extra_weight: int = 15):
        super().__init__(spaceship)
        self.weapon_name = weapon_name
        self.extra_attack = extra_attack
        self.extra_weight = extra_weight

    @override
    def attack_get(self) -> int:
        return self._spaceship.attack_get() + self.extra_attack

    @override
    def weight_get(self) -> int:
        return self._spaceship.weight_get() + self.extra_weight

    @override
    def details_get(self) -> str:
        return f"{self._spaceship.details_get()}, {self.weapon_name}"
