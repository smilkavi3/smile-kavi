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


# check the string contain only  binary value of 1 and 0:1
# n="101"
# l=len(n)
# for i in range(0,l):
#   if (n[i]=="1" or n[i]=="0"):
#     print("Binary 1")
#   else:print("not Binary 0")
  
# Removing even index numbers:2
# s="ocean"
# l=len(s)
# for i in range(0,l,2):
#   print(s[i],end="")
  
# string contain same character:3
# s="ggg"
# l=len(s)
# for i in range(0,l):
#   if s[i]!=s[0]:
#     print("False")
#   else:
#     print("true")

# prime number:4
# n=int(input("Enterr number"))
# if n>1:
#  for i in range(2,n):
#   if n%i==0:
#     print("Not prime",n)
#     break
#   else:
#     print("prime",n)

# lower case to upper case:5
# s="kavi"
# l=len(s)
# for i in range(0,l):
#   s1=s[i].upper()
#   print(s1,end="")

# upper case to lower case:6
# s="KAVI"
# l=len(s)
# for i in range(0,l):
#   s1=s[i].lower()
#   print(s1,end="")

# print the number in given alphanumeric string:7
# s="AA1896d23cBb4"
# l=len(s)
# for i in range(0,l):
#   if (s[i]>="0"and s[i]<="9"):
#     print(s[i],end="")

# converting upper to lower case:8
# s="ProGr ammiNg"
# l=len(s)
# s2=""
# for i in range(0,l):
#   if s[i]>="A"and s[i]<="Z":
#     s2+=s[i].lower()
#   elif s[i]>="a"and s[i]<="z":
#     s2+=s[i].upper()
# print(s2,end="")

# frist letters to convert upper case:9
# s="welcome to codeing"
# l=len(s)
# print(s.title())

# Removing vowel in given string:10
# s="Welcome to coding"
# l=len(s)
# for i in range(0,l):
#   if(s[i] not in "aeiouAEIOU"):
#     print(s[i],end="")

  
