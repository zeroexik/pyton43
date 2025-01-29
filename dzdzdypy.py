class Vehicle:
    def __init__(self, make, model, year, mileage):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage

    def get_info(self):
        return f"{self._year} {self._make} {self._model} - Пробег: {self._mileage} км"


class Car(Vehicle):
    def __init__(self, make, model, year, mileage, body_type):
        super().__init__(make, model, year, mileage)
        self._body_type = body_type

    def get_info(self):
        return f"{super().get_info()} - Кузов: {self._body_type}"


class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, payload_capacity):
        super().__init__(make, model, year, mileage)
        self._payload_capacity = payload_capacity

    def get_info(self):
        return f"{super().get_info()} - Грузоподъёмность: {self._payload_capacity} тонн"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, engine_volume):
        super().__init__(make, model, year, mileage)
        self._engine_volume = engine_volume

    def get_info(self):
        return f"{super().get_info()} - Объём двигателя: {self._engine_volume} см³"


class Fleet:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)

    def list_vehicles(self):
        for vehicle in self._vehicles:
            print(vehicle.get_info())

    def find_vehicle(self, make=None, model=None):
        found_vehicles = []
        for vehicle in self._vehicles:
            if (make and vehicle._make == make) or (model and vehicle._model == model):
                found_vehicles.append(vehicle)
        return found_vehicles


if __name__ == "__main__":
    fleet = Fleet()

   
    car = Car("Toyota", "Corolla", 2020, 15000, "Sedan")
    truck = Truck("Volvo", "FH16", 2018, 75000, 25)
    motorcycle = Motorcycle("Yamaha", "MT-07", 2021, 5000, 689)

    fleet.add_vehicle(car)
    fleet.add_vehicle(truck)
    fleet.add_vehicle(motorcycle)

    print("Список всех транспортных средств:")
    fleet.list_vehicles()

    print("\nПоиск по марке 'Toyota':")
    found = fleet.find_vehicle(make="Toyota")
    for vehicle in found:
        print(vehicle.get_info())
    