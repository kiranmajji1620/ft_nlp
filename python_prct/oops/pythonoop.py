class Student:
    def __init__(self, name, house, patronus=None):
        # if not name:
        #     # print("missing name") # can't let the program flow
        #     # sys.exit("missing name") # not good
            # raise ValueError("Missing Name")
        # if house not in ["Gryffindor", "Hufflpuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house
        # self._house = "fda;lkfa"
        # house and _house are completely different attributes. when we say self.house, we call the setter which will indirectly return or set self._house.
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} is from {self.house} and his patronus is {self.patronus}"
    
    def charm(self):
        match self.patronus:
            case"Stag":
                return "S"
            case"Otter":
                return "O"
            case"Jack Russell terrier":
                return "J"
            case _:
                return "_"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    # Getter function
    @property
    def house(self):
        return self._house
    
    # Setter function
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


    @classmethod
    def attendance(clas, name):
        print(name, "is present")

    @classmethod
    def get(cls):
        name = "harry"
        house = "Gryffindor"
        # return Student(name, house)
        return cls(name, house)

def main():
    # student = get_student()
    student = Student.get()
    print(student) #refers to a specific location in memory
    print(student.charm())
    student.house = "Hufflpuff" # this will go through our setter function and undergo checks
    student._house = "pufflHuff" # This will work since we are not calling setter method, we are just changing the underlying instance variable

    print(student)
    print(Student.attendance("harry"))
    # print(student.name)

def get_student():
    name = "Harry"
    house = "Gryffindor"
    patronus = "Stag"
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()