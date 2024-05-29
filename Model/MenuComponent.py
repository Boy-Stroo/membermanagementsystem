from abc import ABC, abstractmethod

class MenuComponent(ABC):

    parent : 'MenuComponent' = None

    @abstractmethod
    def execute(self, *args):
        pass

    def display(self):
        pass