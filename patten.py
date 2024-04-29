# question no:1
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()
# question no:2
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()
# question no:3
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# question no:4
# for i in range(5,0,-1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()
# question no:5
# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()
# question no:6
# for i in range(1,25+1):
    # print("{:2d}".format(i),end=" ")
#     if i%5==0:
#         print()
# question no:7
# for i in range(1,50,2):
#     print("{:2d}".format(i),end="")
#     if (i+1)%10==0:
#         print()
# question no:8
# for i in range(2,50+1,2):
#     print("{:2d}".format(i),end=" ")
#     if i%10==0:
#         print()
#  question no:9
# for i in range(1,6):
#     for j in range(1,6):
#         print("{:2d}".format(i*j),end=" ")
#     print()


# question no:10
# a=1
# for i in range(1,5):
#   for j in range(0,5):
#     if j%2==0:
#       print(i,end=" ")
#     else:
#       print(j,end=" ")
#   print()
#   a+=1


# question no:18
# for i in range(1,5+1):
#     for j in range(1,5+1):
#         print((i+j)%2,end=" ")
#     print()

# question no:19
# for i in range(1,26):
#       a=i%2
#       print(a,end=" ")
#       if i%5==0:
#           print()
# 
# string reversing program
# n="welcome"
# l=len(n)
# for i in range(-1,-l,-1):      
#     print(n[i],end=" ")

# separate the special,albhabet,number character:
# s="**Docoding1234567890everyday##"
# s1=""
# s2=""
# s3=""
# for i in s:
#   if ((i>="a"and i<="z")or(i>="A" and i<="Z")):
#    s1+=i
#   if (i>="0" and i<="9"):
#     s2+=i
#   if i>="!" and i<="+" :
#     s3+=i
# print(s2,end="")
# print()
# print(s1,end="")
# print()
# print(s3,end="")
# print()

# for j in s:
#   if((j>="0" and j<="9")):
#     s2+=j
# print(s2,end="")
# print()

# question no:14
# for i in range(0,5):
#   for j in range(0,5):
#     print("{:2d}".format(j*5+5-i),end=" ")
#   print()
  
  # question no:12
# for i in range(1,6):
#   for j in range(0,5):
#     print(j*5+i,end="  ")
#   print()

# question no:15
# for i in range (0,5):
#   for j in range(0,5):
#     if j%2!=0 :
#       print(j*5+1+i,end=" ")
#     else:
#       print(j*5+5-i,end=" ")
#   print()
# question no:16
# for i in range(1,5):
#   for j in range(5):
#     print("{:2d}".format(j+i),end=" ")
#   print()

# question no:17
# for i in range(1,10,2):
#   for j in range(0,10,2):
#     print("{:2d}".format(i+j),end=" ")
#   print()

# question no:20
# for i in range(1,6):
#   for j in range(1,6):
#     if i%2==0 or j%2==0:
#       print("0",end=" ")
#     else:
#       print("1",end=" ")
#   print()

# question no:13
# for i in range (0,5):
#   for j in range(0,5):
#     if j%2==0 :
#       print(j*5+1+i,end=" ")
#     else:
#       print(j*5+5-i,end=" ")
#   print()


# example:01
# s2="gafd"
# s1="aacdb"
# d=""

# for i in s1:
#   if i not in s2:
#     d+=i
# for j in s2:
#   if j not in s1:
#     d+=j
# print(d)

# example :02
# s1="abcs"
# s2="cxzca"
# o=""

# for i in s1:
#   if i not in s2:
#     o+=i
  
# for j in s2:
#   if j not in s1:
#     o+=j
    
# print(o)

# s="testsample"
# s="output"
# f={}
# for i in s:
#   if i in f:
#     f[i]+=1
#   else:
#     f[i]=1
# print("maximum char of test sample: ",f)
# print()
# print((sorted(f)))

# question no:1
# check the string contain only  binary value of 1 and 0:
# n="101"
# l=len(n)
# for i in range(0,l):
#   if (n[i]=="1" or n[i]=="0"):
#     print("Binary 1")
#   else:print("not Binary 0")
  
# question no:2
# Removing even index numbers:
# s="ocean"
# l=len(s)
# for i in range(0,l,2):
#   print(s[i],end="")
  
# question no:3
# string contain same character:
# s="ggg"
# l=len(s)
# for i in range(0,l):
#   if s[i]!=s[0]:
#     print("False")
#   else:
#     print("true")

# question no:4
# prime number:
# n=int(input("Enterr number"))
# if n>1:
#  for i in range(2,n):
#   if n%i==0:
#     print("Not prime",n)
#     break
#   else:
#     print("prime",n)

# question no:5
# lower case to upper case:
# s="kavi"
# l=len(s)
# for i in range(0,l):
#   s1=s[i].upper()
#   print(s1,end="")

# question no:6
# upper case to lower case:
# s="KAVI"
# l=len(s)
# for i in range(0,l):
#   s1=s[i].lower()
#   print(s1,end="")

# question no:7
# print the number in given alphanumeric string:
# s="AA1896d23cBb4"
# l=len(s)
# for i in range(0,l):
#   if (s[i]>="0"and s[i]<="9"):
#     print(s[i],end="")

# question no:8
# converting upper to lower case:
# s="ProGr ammiNg"
# l=len(s)
# s2=""
# for i in range(0,l):
#   if s[i]>="A"and s[i]<="Z":
#     s2+=s[i].lower()
#   elif s[i]>="a"and s[i]<="z":
#     s2+=s[i].upper()
# print(s2,end="")

# question no:9
# frist letters to convert upper case:
# s="welcome to codeing"
# l=len(s)
# print(s.title())

# question no:10
# Removing vowel in given string:
# s="Welcome to coding"
# l=len(s)
# for i in range(0,l):
#   if(s[i] not in "aeiouAEIOU"):
#     print(s[i],end="")

# counting the letter in given letter and output in form of dictonary 
# s="banana"
# n={}
# for i in s:
#   if i  in n:
#     n[i]=n[i]+1
#   else:
#     n[i]=1
# print(n)


# new task:

# question no:1
# n=int(input("Enter the numbers"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or  i==n-1 or j==0 or j==n-1  :
#       print("* ",end="")
#     else:
#       print("  ",end="")
#   print()
  
#  question :3
# n=int(input("Enter the number"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or i==n-1 or j==n-1 :
#       print("*",end=" ")
#     else:
#       print("#",end=" ")
#   print()
 
# n=int(input("Enter the number"))
# for i in range(n):
#   for j in range(n):
#     if i==j or i==0 or j==0 or i==n-1 or j==n-1   or (i==1 and j==3) or (i==3 and j==1):
#       print("* ",end="")
#     else:
#       print("  ",end="")
#   print()

# question no:2 (square in cross box 7)
# n=int(input("Enter the number"))
# for i in range(n):
#   for j in range(n):
#     if i==j or i==0 or j==0 or i==n-1 or j==n-1   or (i+j==6):
#       print("* ",end="")
#     else:
#       print("  ",end="")
#   print()

# question no:4
# c curve shape:
# for i in range(7):
#   for j in range(7):
#     if i==0 or j==0 or i==6:
#       print("* ", end="")
#   print()

# reverse hill patten :
# n=5
# for i in range(n):
#   for j in range(i+1):
#     print(" ",end=" ") 
#   for k in range(i,n):
#       print("*",end=" ")
#   for l in range(i,n+1):
#     print("*",end=" ")
#   print()
# n=6
# for i in range(n):
#   for j in range(i,n):
#     print(" ",end=" ") 
#   for k in range(1,i+1):
#       print("*",end=" ")
#   for l in range(i+1):
#     print("*",end=" ")
#   print()

# diamond patten:
# n=int(input("Enter number :"))
# for i in range(1,n):
#   for j in range(i,n):
#     print("",end=" ")
#   for k in range(1,i+1):
#     print("*",end=" ")
#   print()
  
# for i in range(1,n):
#   for j in range(i+1):
#     print("",end=" ")
#   for l in range(i,n-1):
#     print("*",end=" ")
#   print()

# print arrow mark:
# n=7
# for i in range(n):
#   for j in range(n):
#     if i==3 or (i==2 and j==5) or (i==1 and j==4) or (i==4 and j==5) or(i==5 and j==4):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# alphabet B patten:
# n=5
# for i in range(n):
#   for j in range(n):
#     if   (i==0 and j<=3) or (i==4 and j<=3) or i==2 or j==0 or (i==1 and j==4) or (i==3 and j==4) :
#       print("*", end=" ") 
#     else:
#       print(" ", end=" ")
#   print()

# different star patten:
# n=7
# for i in range(n):
#   for j in range(n):
#     if j==3 or i==3 or (i==0 and j>=3) or (j==0 and i<=3) or(i==6 and j<=3) or (j==6 and i>=3):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# A patten:
# for i in range(5):
#   for j in range(9):
#     if (i==0 and j==4) or (i==1 and j==3) or (i==2 and 2<=j<=6) or (i==3 and j==1) or (i==4 and j==0) or (i==1 and j==5) or (i==3 and j==7) or (i==4 and j==8):
#       print("*", end=" ")
#     else:
#       print(" ",end=" ")
#   print()


for i in range(7):
  for j in range(9):
    if (i==0 and 0<j<=2 )or(i==0 and 6<=j<=7)or(i==1 and j<=3)or(i==1 and 5<=j<=9)or(i=):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


    
