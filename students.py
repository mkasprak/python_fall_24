# Class definition
class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value

    def set_grade_level(self, value):
        self.__grade_level = value

    def student_info(self):
        print(f"{self.__first_name}, {self.__last_name}, Student ID: {
              self.__student_id}, {self.__grade_level}")

     # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))


def main():
    me = Student("Ducktor", "Quacksalot", "009234", "Sophomore")
    me.student_info()
    me.print_student_details()
    me.get_grade_level()

    me.set_grade_level("Ducktorate")
    me.student_info()

    student = Student("Jane", "Doe", "12345")

    # True  SEE INFO ON NAME MANGLING IN LESSON
    print(hasattr(student, "_Student__first_name"))
    print(hasattr(student, "_Student__middle_name"))  # False


main()
