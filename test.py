from abc import ABC , abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Motorcycle(ABC):
    @abstractmethod
    def ride(self):
        pass


class Seban(Car):
    def drive(self):
        print("sedan is driving")

class SUV(Car):
    def drive(self):
        print("SUV is driving")


class SportBike(Motorcycle):
    def ride(self):
        print("Riding a SportBike")


class CreateFactory(ABC):
    @abstractmethod
    def car_creator(car_name):
        if car_name =="Seban":
            return Seban()
        elif car_name == "SUV":
            return SUV()
        else:
            print( InvalidValue(f"name {car_name} Invalid!!!")) 
    def motor_creator(self,motor_name):
        if motor_name =="Seban":
            return Seban()
        elif motor_name == "SUV":
            return SUV()
        else:
            return InvalidValue(f"name {motor_name} Invalid!!!")

class InvalidValue(Exception):
    pass


if __name__ == "__main__":
    C_suv = CreateFactory.car_creator(car_name="UV")
