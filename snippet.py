class Student:
    name = []

    def set_name(self, student_name):
        self.name.append(student_name)
        return len(self.name) - 1

    def get_name(self, student_num):
        if student_num >= len(self.name):
            return 'There is no such student'
        else:
            return self.name[student_num]


if __name__ == '__main__':
    student = Student()
    print('Student Stefan has been added with number ', student.set_name('Stefan'))
    print('Student associated with number 0 is ', student.get_name(0))