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
students=db["students"]    

def add_one_student():
    while True:
        roll_number = input("Enter student roll number: ")
        name = input("Enter student name: ").upper()
        age = int(input("Enter student age: "))
        gender = input("Enter student gender: ").upper()
        grade = input("Enter student grade: ").upper()
        student = {"Roll_number": roll_number, "Name": name, "Age": age, "Gender" : gender, "Grade": grade}
        students.insert_one(student)
        print("Student added successfully.")
        choose = input(" continue to add another  students? [yes/no] : ")
        if choose.lower() != "yes":
           break

def add_may_student():
    num_students = int(input("Enter the number of students to add: "))
    details = []
    for i in range(num_students):
        roll_number = input(f"Enter roll number for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ").upper()
        age = int(input(f"Enter age for student {i+1}: "))
        gender = input(f"Enter gender for student {i+1}: ").upper()
        grade = input(f"Enter grade for student {i+1}: ").upper()
        detail = {
            "Roll_number": roll_number,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Grade": grade,
            
        }
        details.append(detail)
        print("-"*20)

    students.insert_many(details)
    print("Students added Successfully.")
        
def view_student():
    a=list(students.find())
    if a:
     for student in a:
        roll_number =student.get("Roll_number","")
        name =student.get("Name","")
        age=student.get("Age","")
        grade=student.get("Grade","")
        gender=student.get("Gender","")
        print("| {:<10} | {:<15} | {:<5} | {:<10} | {:<10} ".format(a["Roll_number"],a["Name"],a["Age"],a["Grade"],a["Gender"]))
    else:
        print("not found")

def statement(i):
 print("| {:<10} | {:<15} | {:<5} | {:<10} | {:<10} ".format(
        i["Roll_number"],
        i["Name"],
        i["Age"],
        i["Gender"],
        i["Grade"]))
def find_one_student():
    roll_number=input("enter the roll_number: ")
    b=students.find_one({"Roll_number":roll_number})
    print("| {:<10} | {:<15} | {:<5} | {:<10} | {:<10} ".format(b["Roll_number"],b["Name"],b["Age"],b["Grade"],b["Gender"]))
    
def find_many_student():
    grade=input("enter the grade: ")
    b=students.find({"Grade":grade})
    num_students = students.count_documents({})
    if num_students > 0:
        print(f"Students in grade {grade}:")
        print("| {:<10} | {:<15} | {:<5} | {:<10} | {:<10}  ".format(
            "Roll Number","Name","Age","Gender","Grade"
        ))
        print("-" * 110)
        for i in b:
            statement(i)
    else:
         print("Gread not found")   


def update_student():
    while True:
        roll_number = input("Enter the roll number of student to update: ")
        query = students.find_one({"Roll_number": roll_number})
        if query:
            print("1. Name\n2. Age\n3. Gender\n4. Grade\n5. Subjects")
            query = int(input("Choose any number from above to update the details of the student: "))
            if query == 1:
                new_name = input("Enter new name: ")
                students.update_one({"Roll_number": roll_number}, {"$set": {"Name": new_name}})
                print("Name updated successfully.")
            elif query == 2:
                new_age = int(input("Enter new age: "))
                students.update_one({"Roll_number": roll_number}, {"$set": {"Age": new_age}})
                print("Age updated successfully.")
            elif query == 3:
                new_gender = input("Enter new gender: ")
                students.update_one({"Roll_number": roll_number}, {"$set": {"Gender": new_gender}})
                print("Gender updated successfully.")
            elif query == 4:
                new_grade = input("Enter new grade: ")
                students.update_one({"Roll_number": roll_number}, {"$set": {"Grade": new_grade}})
                print("Grade updated successfully.")
            elif query == 5:
                new_subjects = input("Enter new subjects (comma-separated): ").split(",")
                students.update_one({"Roll_number": roll_number}, {"$set": {"Subjects": new_subjects}})
                print("Subjects updated successfully.")
            else:
                print("Number out of range.")
        else:
            print("Roll number not found.")
        
        choice = input("Do you want to update another student? (yes/no): ")
        if choice.lower() != 'yes':
            break


         
def delet_one_student():
  while True:  
      a=input("enter student: ")
      if a:
          students.delete_one({"Name":a})
          print("Delet the student successfully")
      else:
          print("student not found")
          
      option=input("continue to delet another student yes of no :")
      if option!="yes":
          break
          
def delet_many_student():
      c=input("enter student grade: ")
      if c:
          students.delete_many({"Grade":c})
          print("Delet the student successfully")
      else:
          print("student not found")
          
      

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
            
if __name__ == "__main__" :
    main()      