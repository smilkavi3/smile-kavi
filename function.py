# function with two parameter and two arguments:
# def function_name(name,age):
#     print("my name is "+name+"and age is "+age)
# function_name("asoon","25")

# unknown num of key and arguments and i loop the function:
# def function_name(**name):
#    for i in name:
#     print("my name is "+name[f"{i}"])
# function_name(std1="asoon",std2="kavi",std3="gowtham",std4="arvind")

# using format string and multiplay the name in two times:
def multiply(name,a):
    for i in range(a):
     return (f"{name*a}\n")
    
c=multiply("kavi",2)
print(c)