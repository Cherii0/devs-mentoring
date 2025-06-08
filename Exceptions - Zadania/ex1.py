
class FileHandler:
    def __init__(self, file_path=None, no_connectors=None, max_file_size=None):
        self._file_path = file_path
        self._no_connectors = no_connectors
        self._max_file_size = max_file_size

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
       if len(value) == 0:
         raise ValueError("Pusty string")
       else:
         self._file_path = value



    @property
    def no_connectors(self):
        return self._no_connectors

    @no_connectors.setter
    def no_connectors(self, value):
        if not 0 < value < 11:
            raise ValueError("max 10 connectors")
        else:
            self._no_connectors = value

    @property
    def max_file_size(self):
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, value):
        if isinstance(value, int):
            if 1000 <= value <= 9999:
                self._max_file_size = value
            else:
                raise ValueError("max_file_size musi byc 4 cyfrowa liczba")
        else:
            raise ValueError("podany argument to nie liczba")
        self._max_file_size = value

    def read_content(self):
        print("reading content")


    def save_to_file(self):
        print("saving to file")


def main():
    file_handler = FileHandler()
    file_handler.max_file_size = 3311
    file_handler.no_connectors = 3
    file_handler.file_path = '/path'

    print(file_handler.__dict__)

if __name__ == "__main__":
    main()
