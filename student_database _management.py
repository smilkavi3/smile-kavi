from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kaviyarasan:xRARocJ5p7doixAV@cluster0.heojidf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db=client["school"]
students=["student"]    

def add_one_student():
    for i in range(1):
        roll_num=input("Enter Roll num of student: ")
        name=input("Enter name of student: ")
        age= input("Enter student age: ")
        std=input("Enter student class: ")
        gender=input("Enter student gender: ")
        detail={
            "roll_num":roll_num,
            "name":name,
            "age":age,
            "std":std,
            "gender":gender,
        }
        students.insert_one(detail)
        
def add_may_student():
    n=input("enter number of student to add: ")
    details=[]
    for i in range():
        roll_num=input("Enter Roll num of student: ")
        name=input("Enter name of student: ")
        age= input("Enter student age: ")
        std=input("Enter student class: ")
        gender=input("Enter student gender: ")
        detail={
            "roll_num":roll_num,
            "name":name,
            "age":age,
            "std":std,
            "gender":gender,
        }
        details.append(detail)
        students.insert_many(details)
        
def view_student():
    a=list(students.find())
    for i in a:
        roll_num=students.get("roll_num","")
        name=students.get("name","")
        age=students.get("age","")
        std=students.get("std","")
        
def find_one_student():
    roll_num=input("enter the roll_num: ")
    b=students.find_one({"roll_num":roll_num})
    print(b)
def find_many_student():
    pass   

def update_student():
 while True:  
  num=students.find_one(input("enter roll_num of student: "))
  if num: 
    print("1.Roll_num\n2.Name\n3.age\n4.std\n5.gender")
    choice=input("enter your choice: ")
    if choice==1:
        roll_num=input("enter roll num: ")
        students.updade({"roll_num":roll_num},{"$set":{"roll_num":roll_num}})
        print("Roll_num update done")
    elif choice==2:
        name=input("enter student name: ")
        students.updade({"roll_num":roll_num},{"$set":{"name":name}})
        print("Name update done")
    elif choice==3:
        age=input("enter student age: ")
        students.update({"roll_num":roll_num},{"$set":{"age":age}})
        print("Age update done")
    elif choice==4:
        std=input("enter student std: ")
        students.update({"roll_num":roll_num},{"$set":{"std":std}})
        print("std update done")
    elif choice==5:
        gender=input("enter student gender: ")
        students.update({"roll_num":roll_num},{"$set":{"gender":gender}})
        print("gender update done")
    else:
        print("out of range")
  else:
    print("choice correct option")
      
    n=input("enter do you want continu yes or no: ")     
    if n.lower()!="yes":
      break
         
def delet_one_student():
    c=input("enter student roll num: ")
    if c:
        

def delet_many_student():
    pass

def main():
    while True:
        print("1.Add one student ")
        print("2.Add many student ")
        print("3.View  student ")
        print("4.Find one student ")
        print("5.Find many student ")
        print("6.Update  student ")
        print("7.Delet one student ")
        print("8.Delet many student ")
        print("9.Exit ")
        
        option=int(input("Enter your option:"))
        
        if option==1:
            add_one_student()
        elif option==2:
            add_may_student()
        elif option==3:
            view_student()
        elif option==4:
            find_one_student()
        elif option==5:
            find_many_student()
        elif option==6:
            update_student()    
        elif option==7:
            delet_one_student()
        elif option==8:
            delet_many_student()
        elif option==9:
            break
        else:
            print("Invalid option and enter correct option")
            
if __name__=="__main__":
    main()         
    