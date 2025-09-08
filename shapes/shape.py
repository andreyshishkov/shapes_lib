from abc import abstractmethod, ABC


class Shape(ABC):

    @abstractmethod
    def get_square(self):
        pass
