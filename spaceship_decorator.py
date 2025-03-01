from typing import override
from abc import ABC, abstractmethod
from ispaceship import ISpaceship


class SpaceshipDecorator(ISpaceship, ABC):

    def __init__(self, spaceship: ISpaceship):
        self._spaceship = spaceship

    @override
    def get_attack(self) -> int:
        return self._spaceship.get_attack()

    @override
    def get_defense(self) -> int:
        return self._spaceship.get_defense()

    @abstractmethod
    def get_weight(self) -> int:
        pass

    @abstractmethod
    def get_details(self) -> str:
        pass

    def __str__(self) -> str:
        return (f"{self.get_details()} "
                f"[Attack: {self.get_attack()}, "
                f"Defense: {self.get_defense()}, "
                f"Weight: {self.get_weight()}]")

