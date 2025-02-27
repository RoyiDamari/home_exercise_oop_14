from abc import ABC, abstractmethod


class ISpaceship(ABC):
    @abstractmethod
    def attack_get(self) -> int:
        pass

    @abstractmethod
    def defense_get(self) -> int:
        pass

    @abstractmethod
    def weight_get(self) -> int:
        pass

    @abstractmethod
    def details_get(self) -> str:
        pass
