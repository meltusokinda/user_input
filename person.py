class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
Person1 =  Person("James", 25, "male" )
#Calling the introduce method to display the person`s information`
Person1.introduce()