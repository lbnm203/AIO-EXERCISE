class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def describe(self):
        return f'Name: {self.name} - YoB: {self.yob}'


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f'Student - {super().describe()} - Grade: {self.grade}'


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f'Doctor - {super().describe()} - Specialist: {self.specialist}'


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f'Teacher - {super().describe()} - Subject: {self.subject}'


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        ward_show = f'Ward Name: {self.name}\n'
        for person in self.people:
            ward_show += f'{person.describe()}\n'
        return ward_show

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = []
        for person in self.people:
            if isinstance(person, Teacher):
                teachers.append(person)
        if not teachers:
            return None
        total_yob = sum(teacher.yob for teacher in teachers)
        return total_yob / len(teachers)


# 2(a)
student1 = Student(name=" studentA ", yob=2010, grade="7")
print(student1.describe())

teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
print(teacher1.describe())

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
print(doctor1.describe())

# 2(b)
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.describe())

# 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
print(ward1.describe())

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
