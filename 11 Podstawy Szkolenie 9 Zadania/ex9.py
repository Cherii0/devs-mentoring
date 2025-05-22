import datetime


class Tank:
    logs = {}

    def __init__(self, tank_name, volume):

        if volume < 0:
            print("Negative volume given")
            return

        if tank_name == "":
            print("No tank name given")
            return

        self.__tank_name = tank_name
        self.__volume = volume
        self.__present_volume = 0


    @staticmethod
    def check_state(tank):

        given_tank_operations = []
        given_tank_volumes = []

        for log in Tank.logs.values():
            if tank.get_name() == log["tank"] and log["status"] == "done":
                given_tank_operations.append(log)


        for operation in given_tank_operations:
            if operation["operation"] == "pour_water":
                given_tank_volumes.append(operation["water_vol"])
            elif operation["operation"] == "pour_out_water":
                given_tank_volumes.append(-operation["water_vol"])
            else:
                given_tank_volumes.append(operation["water_vol"])

        expected = tank.get_present_volume()
        historic_based = sum(given_tank_volumes)

        if expected == historic_based:
            print(f"tank {tank.get_name()} current water {expected} is same as historic based {historic_based}")
        else:
            print(f"tank {tank.get_name()} current water {expected} is not same as historic based {historic_based}")


    @staticmethod

    def show_most_given_operations(operation_type):

        most_operations = {}

        for log in Tank.logs.values():
            if log["operation"] == operation_type:
                if log["tank"] not in most_operations.keys():
                    most_operations[log["tank"]] = 1
                else:
                    most_operations[log["tank"] ] += 1

        most_operation_tank = (sorted( most_operations.items(), key = lambda x : x[1]))[-1][0]


        print(f"most operations of type {operation_type} belongs to {most_operation_tank}")


    @staticmethod
    def show_most_undone_operations():
        undone_operations = {}

        for log_attr in Tank.logs.values():
            if log_attr["status"] == "undone":
                if log_attr["tank"] in undone_operations.keys():
                    undone_operations[log_attr["tank"]] += 1
                else:
                    undone_operations[log_attr["tank"]] = 1

        # sorting tuples by key[1] means values of each tuple
        most_undone = (sorted( undone_operations.items(), key = lambda x : x[1]))[-1][0]
        print(f"most undone operations on tank named : {most_undone}")


    @staticmethod
    def describe_logs():
        print("------------------logs------------------")
        for log_no, log_attr in Tank.logs.items():
            print(log_no, log_attr)

    @staticmethod
    def find_empty_tanks(*tanks):

        empty_tanks = []

        for tank in tanks:
            if int(tank.get_present_volume()) == 0:
                empty_tanks.append(tank.get_name())

        return f"empty tanks : {empty_tanks}"


    @staticmethod
    def find_greatest_amount_water(*tanks):

        greatest_water_amount = tanks[0].get_present_volume()
        greatest_water_tank = tanks[0]

        for tank in tanks:
            tank_amount = tank.get_present_volume()
            if tank_amount > greatest_water_amount:
                greatest_water_amount = tank_amount
                greatest_water_tank = tank

        return f"most water contains tank : {greatest_water_tank.get_name()} with {greatest_water_amount} liters"


    @staticmethod
    def find_most_filled(*tanks):

        most_filled_pct = ( tanks[0].get_present_volume() / tanks[0].get_volume() ) * 100
        most_filled_tank = tanks[0]

        for tank in tanks:
            filled_pct = ( tank.get_present_volume() / tank.get_volume() ) * 100
            if filled_pct > most_filled_pct:
                most_filled_pct = filled_pct
                most_filled_tank = tank


        return f"most filled tank : {most_filled_tank.get_name()} with {int(most_filled_pct)} percent "



    def pour_water(self, volume):

        log_input = {"date-time": datetime.datetime.now().strftime("%c"),
                     "operation": "pour_water",
                     "tank": self.__tank_name,
                     "water_vol": volume,
                     "status": "undone"}

        if self.__present_volume + volume > self.__volume:
            print("Too much volume given")
            Tank.logs[len(Tank.logs) + 1] = log_input
            return
        elif volume < 0:
            print("Negative volume")
            Tank.logs[len(Tank.logs) + 1] = log_input
            return
        else:
            log_input["status"] = "done"
            Tank.logs[len(Tank.logs) + 1] = log_input
            self.__present_volume += volume

    def pour_out_water(self, volume):

        log_input = {"date-time": datetime.datetime.now().strftime("%c"),
                     "operation": "pour_out_water",
                     "tank": self.__tank_name,
                     "water_vol": volume,
                     "status": "undone"}


        if volume > self.__present_volume:
            print("Too much volume to pour out")
            Tank.logs[len(Tank.logs) + 1] = log_input
            return 0
        elif volume < 0:
            print("Negative volume")
            Tank.logs[len(Tank.logs) + 1] = log_input
            return 0
        else:
            log_input["status"] = "done"
            Tank.logs.update({len(Tank.logs) + 1 : log_input})
            self.__present_volume -= volume
            return volume

    def transfer_water(self, from_tank, volume):

        log_input = {"date-time": datetime.datetime.now().strftime("%c"),
                     "operation": "transfer_water",
                     "tank": self.__tank_name,
                     "water_vol": volume,
                     "status": "undone"}

        if volume < 0:
            Tank.logs[len(Tank.logs) + 1] = log_input
            print("Negative volume given")
            return
        elif from_tank.get_present_volume() < volume:
            Tank.logs[len(Tank.logs) + 1] = log_input
            print(f"tank {from_tank.get_name()} has too little water")
            return
        else:
            from_tank.pour_out_water(volume)
            log_input["status"] = "done"
            Tank.logs[len(Tank.logs) + 1] = log_input
            self.__present_volume += volume


    def get_present_volume(self):
        return self.__present_volume

    def get_volume(self):
        return self.__volume


    def get_name(self):
        return self.__tank_name




def main():
    tank1 = Tank("tank1", 100)
    tank2 = Tank("tank2", 300)
    tank3 = Tank("tank3", 300)

    print(f"before filling tanks :  {tank1.get_present_volume()} liters, {tank2.get_present_volume()} liters,"
          f" {tank3.get_present_volume()} liters")

    tank1.pour_water(65)
    tank1.pour_water(15)
    tank2.pour_water(165)

    print(f"after filling tanks :    {tank1.get_present_volume()} liters, {tank2.get_present_volume()} liters"
          f" {tank3.get_present_volume()} liters")

    tank1.pour_out_water(20)
    tank2.pour_out_water(125)
    tank2.pour_out_water(12)
    tank2.pour_out_water(1)

    print(f"after pour out :   {tank1.get_present_volume()} liters, {tank2.get_present_volume()} liters"
          f" {tank3.get_present_volume()} liters")

    tank2.transfer_water(tank1, 45)
    # undone operations
    tank1.transfer_water(tank1, 425)
    tank2.transfer_water(tank1, 1111)
    tank2.transfer_water(tank1, 1111)
    print(f"after water transfer : {tank1.get_present_volume()} liters, {tank2.get_present_volume()} liters"
          f" {tank3.get_present_volume()} liters")

    print(Tank.find_greatest_amount_water(tank1, tank2, tank3))
    print(Tank.find_most_filled(tank1, tank2, tank3))
    print(Tank.find_empty_tanks(tank1, tank2, tank3))

    # logs
    Tank.describe_logs()

    Tank.show_most_undone_operations()
    Tank.show_most_given_operations("transfer_water")
    Tank.show_most_given_operations("pour_out_water")
    Tank.show_most_given_operations("pour_water")

    # check expected state against operations history
    Tank.check_state(tank1)
    Tank.check_state(tank2)
    Tank.check_state(tank3)


if __name__ == "__main__":
    main()
