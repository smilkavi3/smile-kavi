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
