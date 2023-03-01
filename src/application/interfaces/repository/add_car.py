from abc import ABC, abstractmethod

from src.domain.schemas import Car

from src.domain.usecases import AddCarModel


class AddCarRepositoryInterface(ABC):
    """Interface to Add Car Repository"""

    @abstractmethod
    def add(self, car: AddCarModel) -> Car:
        """abstractmethod"""

        raise NotImplementedError()
