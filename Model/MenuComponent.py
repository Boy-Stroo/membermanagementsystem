from abc import ABC, abstractmethod

class MenuComponent(ABC):

    @abstractmethod
    def execute(self, *args):
        pass

    def display(self):
        pass