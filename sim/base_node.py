from abc import ABC, abstractmethod
from sim.stream import Stream


class UnitOp(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def step(self, dt: float, inflows: dict) -> dict:
        ...

    @abstractmethod
    def get_state(self) -> dict:
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"
