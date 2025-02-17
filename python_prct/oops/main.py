class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

s = Student("kiran", 21)
print(s.name)