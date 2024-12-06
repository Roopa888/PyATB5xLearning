from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass
    def set_gear0(self):
        print("Ready to change the gear ")


class Engine(GearBox):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def set_gear(self):
        self.set_gear0()
        print("Gear box is ready")


class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def drive(self):
        self.start()
        self.set_gear()
        self.stop()


car_obj = Car()
car_obj.drive()
