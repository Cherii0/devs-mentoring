

class Program:

    def __init__(self, path):
        self.file_path = path
        self.data_raw = []
        self.data_parsed = {}
        self.data_filtered = []
        self.contrast_pixels = 0
        self.pixel_lists = []



        with open(self.file_path, "r") as file:
            self.data_raw = file.readlines()

        self.most_bright_pixel_value = 0
        self.most_bright_pixel_row = 0

        self.most_dark_pixel_value = 255
        self.most_dark_pixel_row = 0



    def parse_data(self):
        for idx, row in enumerate(self.data_raw, start=1):
            self.data_parsed[idx] = row.replace("\n", "").split(" ")

        # convert strings integers into int datatype
        for key, value in self.data_parsed.items():
            for idx, pixel in enumerate(value):
                self.data_parsed[key][idx] = int(pixel)



    def point_most_bright_dark_pixels(self):
        for key, value in self.data_parsed.items():

            if max(self.data_parsed[key]) >= self.most_bright_pixel_value:
                self.most_bright_pixel_value = max(self.data_parsed[key])
                self.most_bright_pixel_row = key

            if min(self.data_parsed[key]) <= self.most_dark_pixel_value:
                self.most_dark_pixel_value = min(self.data_parsed[key])
                self.most_dark_pixel_row = key

        print(f"most bright pixel value is : {self.most_bright_pixel_value} at line : {self.most_bright_pixel_row}")
        print(f"most dark pixel value is : {self.most_dark_pixel_value} at line : {self.most_dark_pixel_row}")

    def point_contrast_pixels(self):

        diff = 128

        for value in self.data_parsed.values():
            self.pixel_lists.append(value)


        for row in range(len(self.pixel_lists)):
            for pixel in range(len(self.pixel_lists[row])):
                current_pixel = self.pixel_lists[row][pixel]

                if row == 0:
                    top_pixel = current_pixel
                else:
                    top_pixel = self.pixel_lists[row - 1][pixel]


                if row == (len(self.pixel_lists)-1):
                    bottom_pixel = current_pixel
                else:
                    bottom_pixel = self.pixel_lists[row + 1][pixel]


                if pixel == 0:
                    before_pixel = current_pixel
                else:
                    before_pixel = self.pixel_lists[row][pixel - 1]

                if pixel == len(self.pixel_lists[row])-1:
                    after_pixel = current_pixel
                else:
                    after_pixel = self.pixel_lists[row][pixel + 1]


                if abs(current_pixel - top_pixel) > diff:
                    contrast = True
                elif abs(current_pixel - bottom_pixel) > diff:
                    contrast = True
                elif abs(current_pixel - after_pixel) > diff:
                    contrast = True
                elif abs(current_pixel - before_pixel) > diff:
                    contrast = True
                else:
                    contrast = False

                if contrast:
                    self.contrast_pixels += 1

        print(f"contrast pixels : {self.contrast_pixels}")



def main():
    program = Program("dane.txt")
    program.parse_data()
    program.point_most_bright_dark_pixels()
    program.point_contrast_pixels()

if __name__ == "__main__":
    main()
