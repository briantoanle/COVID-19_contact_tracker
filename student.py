class Student:
    student_id = ""
    name = ""
    is_sick = False
    def __init__(self, student_id, name, is_sick):
        self.student_id = student_id
        self.name = name
        self.is_sick = is_sick

    def __str__(self):
        return self.name + f' ({self.student_id})'

    def __repr__(self):
        return "'" + self.__str__() +"'"

    def is_valid_id(student_id):
        if len(student_id) == 9 and int(student_id[:3]) == 260:
            return True
        return False

larry = Student('260745567', 'Larry', True)

print(Student.is_valid_id('260745567'))
print(Student.is_valid_id('26O1543s'))



