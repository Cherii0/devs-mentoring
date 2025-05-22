
class EndStation:

    def __init__(self, station_name, station_type):
        self.vehicles = []
        self.name = station_name
        self.type = station_type

    def __str__(self):
        message = f"station name : {self.name}, station type : {self.type}, wehicles : "
        message += "\n"
        # shared part within all vehicles
        for vehicle in self.vehicles:
            message += f"    {vehicle}"
            message += "\n"

        # specified part for bus or tram
        if self.type == "bus":
            message += (f"total fuel usage by {len(self.vehicles)} buses :"
                        f" {sum([vehicle.get_fuel_usage() for vehicle in self.vehicles])}")
        else:
            message += f"total carriages : {sum([vehicle.get_carriage_no() for vehicle in self.vehicles])}"

        return message

    def stop_at_end_station(self, vehicle):

        if vehicle.get_type() == self.type:
            self.vehicles.append(vehicle)
        else:
            print("Wrong station")


class Vehicle:

    def __init__(self, max_speed, vehicle_no, end_station, vehicle_type):
        if vehicle_type not in ["bus", "tram"]:
            print("Wrong vehicle type")
            self.vehicle_type = "unknown"

        self.max_speed = max_speed
        self.vehicle_no = vehicle_no
        self.end_station = end_station
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"vehicle no {self.vehicle_no} with max speed : {self.max_speed} and end station : {self.end_station}"

    def get_type(self):
        return self.vehicle_type


class Tram(Vehicle):

    def __init__(self, max_speed, vehicle_no, end_station, vehicle_type, carriage_no):
        super().__init__(max_speed, vehicle_no, end_station, vehicle_type)
        # attribute unique for this type of vehicle
        self.carriage_no = carriage_no


    def get_carriage_no(self):
        return self.carriage_no


class Bus(Vehicle):

    def __init__(self, max_speed, vehicle_no, end_station, vehicle_type, fuel_usage):
        super().__init__(max_speed, vehicle_no, end_station, vehicle_type)
        # attribute unique for this type of vehicle
        self.fuel_usage = fuel_usage

    def get_fuel_usage(self):
        return self.fuel_usage


def main():

    bus_station = EndStation("Gaj", "bus")
    tram_station = EndStation("Pilchowice", "tram")

    bus176 = Bus(120, 176, "Gaj", "bus", 3000)
    bus128 = Bus(120, 128, "Gaj",  "bus", 4000)
    bus111 = Bus(140, 111, "Gaj", "bus",3400)

    tram19 = Tram(40, 11, "Pilchowice","tram", 3)
    tram8 = Tram(40, 8, "Pilchowice", "tram",3)
    tram7 = Tram(40, 7, "Pilchowice", "tram", 2)

    bus_station.stop_at_end_station(bus176)
    bus_station.stop_at_end_station(bus111)
    bus_station.stop_at_end_station(bus128)

    tram_station.stop_at_end_station(tram19)
    tram_station.stop_at_end_station(tram7)
    tram_station.stop_at_end_station(tram8)

    print(bus_station)
    print(tram_station)



if __name__ == '__main__':
    main()
