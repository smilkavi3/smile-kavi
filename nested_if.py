a=int (input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if(a>b) and (a>c):
    print("A is greater")
    if(c>b):
        print("c is greater")
else:
    print("b is greater ")
    
    
p=int(input("physics"))
c=int(input("chemistry"))
b=int(input("Biology"))
m=int(input("Mathematics"))
cp=int(input("computer"))
per=(p+c+b+m+cp)/5
print("Percentage=",per)
if(per>=90):
    print("Grade A")
elif(per<=90):
    print("Grade B")
elif(per<=80):
    print("Grade C")
elif(per<=70):
    print("Grade D")
elif(per<=60):
    print("Grade E")
elif(per<=40):
    print("Grade F")
    
s=float(input("Basic Salary"))
if(s<=10000):
    s1=(s*.8)*.2
    print("Gross salary",s1)
if(s<=20000):
    s1=(s*.8)*.2
    print("Gross salary",s1)
if(s>20000):
    s1=(s*.95)*.3
    print("Gross salary",s1)

# to check is triangle:

a=int (input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if (a+b+c)==180:
    print("is triangle")
else:
    print("not triangle")    
    
# To check the triangle types: 
a=int (input("enter number "))
b=int(input("enter number"))
c=int(input("enter number"))

if (a==a and b==c and c==a):
    print("Isosceles triangle") 
elif(a==b and b==c or c==a):
    print("Euilateral triangle")
else:
    print("scalene triangle")   

# to check leap year:
y=int(input("Enter the year"))
if y % 4==0 or y % 100!=0 and y % 400==0:
    print("Leap year")
else:
    print("Comon year")
    

