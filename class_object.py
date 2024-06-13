# class is blue print to creat object (car) and object is (output of car)
# class consist of attributs,functionality
# sir program:
# class Student:
#     # constructor
#     def __init__(self, firstName, lastName, age, location, skills):
#         # attribute
#         self.firstName = firstName
#         print(self)
#         self.lastName = lastName
#         self.age = age
#         self.location = location
#         self.skills = skills
        
  
#     # functionality 
#     def getDetails(self):
#         print("Student Details")
#         print("*" * 10)
#         print("First Name", self.firstName)
#         print("Last Name", self.lastName)
#         print("Age", self.age)
#         print("Location", self.location)
#         print("Skills :")
#         for i in self.skills:
#             print(i)
#         print("*" * 10, end="\n" * 2)
        
#     def getFullName(self):
#         print(self.firstName + " " + self.lastName)
    

# #  a is object
# a = Student(
#     "kaviyarasan", "B.", 22, "Pondy", ["PYTHON", "C" , "JAVA script", "HTML", "CSS", "sass"]
# )


# a.getFullName()
# a.getDetails()

# b.getFullName()
# b.getDetails()


# def power(n,p):

#   if p%2==0:
#     a=power(n,p//2)
#     return a*2
   
   
# c=power(5,2)
# print(c)



# encapsulation:
# Restriction on accessing variables and methods directly and can prevent the accidental modification of data
# two type of variable private and public and protected

#private variable to  access to within the class 

# class Base():
#     def __init__(self):
#         self.__name1="kavi"
#     def name(self):
#         print(self.__name1)
# a=Base()
# a.name()
# print(a.__name1)        

# public can access to outside of the class

# class Base():
#     def __init__(self):
#         self.name1="kavi"
#     def name(self):
#         print(self.name1)
# a=Base()
# a.name()
# print(a.name1)  

# protected variable to access to sub class:
class Base():
    def __init__(self):
        self._name1="kavi"
    def name(self):
        print(self._name1)
class sub(Base):
    pass
a=sub()
a.name()
print(a._name1) 