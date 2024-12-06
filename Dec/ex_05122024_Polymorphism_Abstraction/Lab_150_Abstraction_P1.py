# Abstraction -Hide the details and show only what is required
# Eg:
# Car -key --->--private,tyre--->public
# Method -Car -Engine ,Gera box--->private
# Car -driver=public
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Barks")


obj_dog=Dog("Shera")
obj_dog.make_sound()