# inheritance is five type(1- single inheritance): 
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# abstraction goal is to handle complexity by hiding unnecessary detail from the user 

# single inheritance:

# class Senior_student():
#     def detail(self,name):
#         print(f"name is {name}")
# class Junior_student(Senior_student):
#     pass
# a=Junior_student()
# a.detail("asoon")
 
    
# multiple inheritance:
# class Maths():
#     def name1(self,marks):
#         print("the subject is mathes:",marks)
# class Tamil():
#     def name(self,marks):
#         print("the subject is tamil:",marks)
# class Subjects(Tamil,Maths):
#     pass
# b=Subjects()
# b.name1(24) 

# multilevel inheritance:
# class Add():
#     def addition(self,a,b):
#         print(f"addition is {a} {b}:",a+b)
# class Sub(Add):
#     def subraction(self,a,b):
#         print(f"subraction is {a} {b}:",a-b)
# class Maths(Sub):
#     pass
# o=Maths()
# o.subraction(5,4)
# o.addition(5,4)

# Hierarchical in heritance:
class Base():
    def add(self,a,b):
       return a+b
    def sub(self,a,b):
        print(f"sub of num{a} {b} is:",a-b)
    def multiplay(a,b):
        print(f"multiplay of num{a} {b} is:",a*b)   
class derived1(Base):
    pass
class derived2(Base):
    pass
class derived3(Base):
    pass
p=derived1()
d=p.add(2,8)
print(d)


