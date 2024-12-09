from abc import ABC, abstractmethod


class PC():
    def __init__(self):
        print("PC is initialized")


class MotherBoard():
    def start_motherboard(self):
        print("Mother Board started")


class Ram(ABC):
    @abstractmethod
    def start_Ram(self):
        pass


class Processor(ABC):
    @abstractmethod
    def start_Processor(self):
        pass


class Storage(ABC):
    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def loadOS():
        print("OS is loading")

    def start_Mouse(self):
        print("Mouse is started")

    def use_HeadPhone(self):
        print("Using head phones")
