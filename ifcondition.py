L=input("Enter letters_")
if((L>="a"and L<="z") or (L>="A" and L<="Z")):
    print("alphabet")
else:
    print("Not alphabet")

n=int(input("Enter number_"))
if((n%5==0) and (n%11==0)):
    print("Divisible")
else:
    print("Not divisible")

L=input("Enter letter")
n=int(input("Enter number"))
if(n>0):
    print("Positive number")
elif(n == 0):
    print("The number zero")
else:
    print("Negative number")

n1=float(input("Enter the number"))
n2=int(input("Enter number"))
n3=float(input("Enter number"))
if((n1>n3) and (n1>n2)):
    print("Frist number")
elif(n2>n3):
    print("Scond number")
else:
    print("thrid number")
w=int(input("Enter week number"))
if(w==1):
    print("Monday")
elif(w==2):
    print("Tuesday")
elif(w==3):
    print("Wednesday")
elif(w==4):
    print("Thursday")
elif(w==5):
    print("Friday")
elif(w==6):
    print("Saturday")
elif(w==7):
    print("Sunday")
else:
    print("Invalid")

a=int(input("Amount"))
if(a>=2000):
    print("2000")
else:
    print("0")
if(a==500):
    print("500")
else:
    print("0")
