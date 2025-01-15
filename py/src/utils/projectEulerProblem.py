from abc import ABC, abstractmethod
class ProjectEulerProblem(ABC):
    @abstractmethod
    def solve(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self):
        pass