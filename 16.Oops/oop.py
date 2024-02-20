class Student:
    name = ""  # attributes
    age = 0
    gender = ""

    # Methods
    def display(self):
        print(f"My name is {self.name}")
        print(f"my age is {self.age}")
        print(f"my gender is{self.gender}")

    def setInfo(self):
        self.name: str = input("Enter name = ")
        self.age: int = int(input("Enter age ="))
        self.gender: str = input("Enter gender = ")


s1 = Student()  # s1 is the instance of the class
s1.name = "Akshay"  # assign the value for s1 object for name
s1.age = 28
print(s1.name)  # print the s1 objects name
print(s1.age)
print(s1.gender)

# As you can see to print s1 attributes we need 3 lines of code so to avoid it we have created the method.
s1.display()  # this will print the details using display method
print("__________________")
s2 = Student()
print(s2.name)
print(s2.age)
print(s2.gender)

# now to add the values for each objects we have set the values manually so we can solve this by wriying the below method

s1.setInfo()
s1.display()
