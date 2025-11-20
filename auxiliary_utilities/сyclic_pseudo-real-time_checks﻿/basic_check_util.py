from abc import ABC, abstractmethod


class BasicCheckUtil(ABC):
    @abstractmethod
    def check_state(self):
        ...
