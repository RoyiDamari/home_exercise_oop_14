from typing import override
from abc import ABC, abstractmethod
from ispaceship import ISpaceship


class SpaceshipDecorator(ISpaceship, ABC):

    def __init__(self, spaceship: ISpaceship):
        self._spaceship = spaceship

    @override
    def attack_get(self) -> int:
        return self._spaceship.attack_get()

    @override
    def defense_get(self) -> int:
        return self._spaceship.defense_get()

    @abstractmethod
    def weight_get(self) -> int:
        pass

    @abstractmethod
    def details_get(self) -> str:
        pass

    def __str__(self) -> str:
        return (f"{self.details_get()} "
                f"[Attack: {self.attack_get()}, "
                f"Defense: {self.defense_get()}, "
                f"Weight: {self.weight_get()}]")

