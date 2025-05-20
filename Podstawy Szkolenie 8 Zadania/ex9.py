import json

class Program():

    def __init__(self):
        self.data_parsed = []
        self.data_raw = {}
        self.data_filtered = []
        self.target_keys = ["dn", "speed", "mtu"]

    def read_file(self, filename):

        with open (filename, "r") as file:
            self.data_raw = json.load(file)
            self.data = self.data_raw["imdata"]
            for elem in self.data:
                self.data_parsed.append(elem["l1PhysIf"]["attributes"])

    def parse_data(self):

        for d in self.data_parsed:
            for key in self.target_keys:
                self.data_filtered.append(d[key])


    def show_interface(self):


        print("\n")
        print("Interface Status")
        print("================================================================================")
        print(f"{self.target_keys[0].upper()}                                    Descriptopn          "
              f"  {self.target_keys[1].capitalize()}          {self.target_keys[2].upper()}" )
        print("----------------------------------- ----------------------  -----------  --------")
        for idx in range(0, len(self.data_filtered)-2, 3):
            print(f"{self.data_filtered[idx+0]}                   {self.data_filtered[idx+1]}        {self.data_filtered[idx+2]}")


def main():
    program = Program()
    program.read_file("dane_json.json")
    program.parse_data()
    program.show_interface()


if __name__ == "__main__":
    main()
