# inheritance is five type(1- single inheritance): 
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# class Father:
#     def __init__(self,fname,lname,age):
#         self.frist_name=fname
#         self.last_name=lname
#         self.age=age
#     def fullname(detail):
#         a=detail.frist_name+" "+detail.last_name+ "age is",detail.age
#         print(a) 
          
# class Student(Father):
#     pass


# x = Student("Kavi", "yarasan",23)
# x.fullname()

# multiple inheritance:

# class Father:
#     def fullname(self):
#         print("father")

# class Mother:
#     def fullname(self):
#         print("mother")

# class Child(Father,Mother):
#     pass
# x=Child()
# x.fullname()

# Mother.fullname(x)
# Father.fullname(x)

# multilevel inheritance: derived class access the two base class
# type 1 simple
# class Class1:
#     def m(self):
#         print("In Class1") 
       
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
 
# class Class3(Class2):
#     def m(self):
#          print("In Class3")     
     
# class Class4( Class3):
#     def m(self):
#         print("In Class4")   
 
# obj = Class4()
# obj.m()
 
# Class2.m(obj)
# Class3.m(obj)
# Class1.m(obj)

# type 2 litle complex
# class Vehicle:
#     def __init__(detail,brand):
#         detail.brand=brand
#     def name(detail):
#         print("vehicle name ",detail.brand)
# class Car(Vehicle):
#     def __init__(detail, brand,model):
#         super().__init__(brand)
#         detail.model=model
#     def name(detail):
#         print("model name ",detail.model)
        
# class Honda(Car):
#     def __init__(detail, brand, model,horse_power):
#         super().__init__(brand, model)
#         detail.horse_power=horse_power
#     def name(detail):
#         print("Horse power is ",detail.horse_power)
#     def fullname(detail):
#         print(f"vehicle name is {detail.brand} model name {detail.model} hores powerr is {detail.horse_power} hp")
# x=Honda("tesla","advance_AI",400)
# x.fullname()
# x.name()     

# hybrid inheritance:
 
class shape:
    def draw(self):
        print("draw")
class circle(shape):
    def draw(self):
        # self.mm=mm
        print("drawc")
class square():
    def draw(self):
        print("draws")
c=square()
shape.draw(c)