class Person:
    def __init__(self, name):
        self.name = name
        self.grades = ["0" for _ in range(8)]

    def __str__(self):
        for i in range(len(self.grades)):
            print(f"{i} : {self.grades[i]}")
        # grades = " ".join([g for g in self.grades])
        return f"Person : {self.name}"

    def __len__(self):
        return len(self.grades)
    
    def __add__(self, other):
        return Person(self.name + other.name)
    
    def __getitem__(self, index):
        return self.name[index]

    def __setitem__(self, index, item):
        # print("set item")
        self.grades[index] = item
        
    def __contains__(self, item):
        return item in self.grades
    
    def __repr__(self):
        return f"{self.name}"
    
    def __delitem__(self, index):
        del self.grades[index]

    def __call__(self, num):
        return num*self.name

def main():
    p1 = Person("Sai")
    p1[0] = "A"
    p1[1] = "B"
    p1[2] = "A"
    print(p1)
    print(len(p1))
    del p1[1]
    print(p1)
    del p1[2]
    print(len(p1))
    print(p1)
    print("A" in p1)
    print(p1(5))
    # p2 = Person("Kiran")
    # p3 = p1 + p2
    # print(p3.__repr__())
    # print(p3)

    # print(p3[3])
    # print("S" in p3)
    t = (1, 3, 4)
    print(t.sorted())

if __name__ == "__main__":
    main()
