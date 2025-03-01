from abc import ABC, abstractmethod


class ISpaceship(ABC):
    @abstractmethod
    def get_attack(self) -> int:
        pass

    @abstractmethod
    def get_defense(self) -> int:
        pass

    @abstractmethod
    def get_weight(self) -> int:
        pass

    @abstractmethod
    def get_details(self) -> str:
        pass
