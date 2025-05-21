

class Student:
    def __init__(self, name = "Jan", age = 20, year_attended = 1, subject = "IT", gpa = 4):
        self.name = name
        self.age = age
        self.subject = subject
        self.year_attended = year_attended
        self.gpa = gpa


    def __str__(self):
        return "Student object"

    def describe(self):
        print(f"student o imieniu {self.name} w wieku {self.age} lat uczeszcza na rok"
              f" {self.year_attended} kierunku {self.subject} i posiada "
              f"srednia ocene {self.gpa}")


def main():
    
    # creating objects
    student1 = Student()
    student2 = Student(name = "Bartek", age = 22)
    student3 = Student(name = "Adrian", age = 22, year_attended = 3, subject = "Bioinformatyka", gpa = 3  )
    
    # printing objects attributes
    student1.describe()
    student2.describe()
    student3.describe()


if __name__ == '__main__':
    main()
