

class Member:

    def __init__(self, member_name):
        self.__member_name = member_name
        self.__member_type = self.__class__.__name__

    def introduce(self):
        print(f"Hi my name is {self.__member_name} and I am {self.__member_type}")

    def get_name(self):
        return self.__member_name

class Student(Member):

    def __init__(self, member_name, reason):
        super().__init__(member_name)
        self.__attending_reason = reason

    def introduce(self):
        super().introduce()
        print(f"{self.__attending_reason}\n")


class Instructor(Member):

    def __init__(self, member_name, biography, *args):
        super().__init__(member_name)
        self.__biography = biography
        self.__skills = list(args)


    def add_skill(self, skill):
        if skill in self.__skills:
            print("Already have this skill")
        else:
            self.__skills.append(skill)

    def introduce(self):
        super().introduce()
        print(f"{self.__biography}\n")



class Workshop:

    def __init__(self, date_workshop, subject):
        self.__group_instructors = set()
        self.__roster_students = set()
        self.__date = date_workshop
        self.__subject = subject

    def add_participant(self, member):

        parent = member.__class__.__bases__
        if not isinstance(member, parent):
            print("participant must be Member class")
            return

        if isinstance(member, Instructor):
            self.__group_instructors.add(member)
        else:
            self.__roster_students.add(member)

    def __print_students_roster(self):

        from functools import reduce
        students = [s.get_name() for s in self.__roster_students]
        students_msg = reduce(lambda acc, s : acc + ", " + s, students)
        print(f"The students are : {students_msg}")

    def __print_instructors_group(self):

        from functools import reduce
        instructors = [i.get_name() for i in self.__group_instructors]
        instructors_msg = reduce(lambda acc, i : acc + ", " + i, instructors)
        print(f"The instructors are : {instructors_msg}")

    def print_details(self):

        print(f"The workshop is about {self.__subject}")
        print(f"It has {len(self.__roster_students)} students and " 
                   f"{len(self.__group_instructors)} instructors")

        self.__print_students_roster()
        self.__print_instructors_group()
        print(f"Class runs every {self.__date}")



def main():

    workshop = Workshop("Saturday", "Software engineering")

    student1 = Student("Adrian", "Grateful to be here")
    student2 = Student("Piotr", "I want to make website")
    student3 = Student("Jakub", "Student of software engineering")
    instructor1 = Instructor("Jan", "I enjoy share my software programming knowledge",
                             "Python", "Databricks")

    workshop.add_participant(instructor1)
    workshop.add_participant(student1)
    workshop.add_participant(student2)
    workshop.add_participant(student3)

    student1.introduce()
    student2.introduce()
    student3.introduce()
    instructor1.introduce()

    workshop.print_details()

if __name__ == "__main__":
    main()
