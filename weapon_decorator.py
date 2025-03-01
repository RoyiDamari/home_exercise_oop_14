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
    def get_attack(self) -> int:
        return self._spaceship.get_attack() + self.extra_attack

    @override
    def get_weight(self) -> int:
        return self._spaceship.get_weight() + self.extra_weight

    @override
    def get_details(self) -> str:
        return f"{self._spaceship.get_details()}, {self.weapon_name}"
