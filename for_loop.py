# question no:1
# print frist 10 natural number:
# for i in range(1,11):
#     print(i)
# -----------------------------------------------------------------------------------------------
# sum of frist 10 natural number:
# question no:2
# s=0
# for i in range(1,11):
#     s+=i
# print("sum",s)

# -----------------------------------------------------------------------------------------------

# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n):
#     print(i)
#     s1=s1+i
# print("sum",s1)

# -----------------------------------------------------------------------------------------------

# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n):
#      print(i)
#      s1=s1+i

#      s=s1/10

# print("sum",s1)
# print("average",s)

# -----------------------------------------------------------------------------------------------

# n=int(input("Enter numbers"))
# for i in range(1,5,1):
#  cubeValue=i ** 3
#  print(f"number is {i} and cube value {i} is",cubeValue)
# -----------------------------------------------------------------------------------------------

# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n,1):
#  if(i%2!=0):
#   print(i,"odd")
#   s1+=i
# print("sum",s1) 
# -----------------------------------------------------------------------------------------------
 
# s=15
# for i in range(1,11,1):
#  multiplication=s*i
#  print(f"{s}x{i}",multiplication)
# -----------------------------------------------------------------------------------------------

# s1=1
# s2=2
# s3=3
# s4=4
# s5=5
# s6=6
# s7=7
# s8=8
# s9=9
# s10=10

# t = 0
# m = 1

# for i in range(1,80):
#    t += 1
#    t += 1
#    print(f"{m} x {t} = {m * t}")
#    if(t % 10 == 0):
#     t = 0
#     m += 1
#     print()
# -----------------------------------------------------------------------------------------------
# question no:7

# for i in range(1,51):
#   for j in range(1,11):
#     print(f"{i} x {j} = {i * j}")
#   print()
      
# -----------------------------------------------------------------------------------------------

# s1=1
# for i in range(1,11):
#   m1=s1*i
#   print(f"{i}x{s1}",m1)

# -----------------------------------------------------------------------------------------------

# for i in range(1,11):
#   m2=s2*i
#   print(f"{i}x{s2}",m2)

# -----------------------------------------------------------------------------------------------

# for i in range(1,11):
#     m3=s3*i
#     print(f"{i}x{s3}",m3)
# -----------------------------------------------------------------------------------------------
# question no:9
# a="*"
# for i in range(1,6):
#      print(a*i)

# -----------------------------------------------------------------------------------------------
# question no:10

# for i in range(1,2):
#   print(i)
#   for m in range(2,3):
#     print(i,m)
#     for j in range(3,4):
#       print(i,m,j)
#       for l in range(4,5):
#         print(i,m,j,l)
# -----------------------------------------------------------------------------------------------
# question no:10

# rowCountEnd = 1
# inc = 0
# for i in range(10):
#      inc += 1
#      print(inc, end = " ")
#      if(rowCountEnd == inc):
#           rowCountEnd += 1
#           inc = 0
#           print()

# -----------------------------------------------------------------------------------------------
  # question no:10
   
# for i in range(1,11):
#      for j in range(1,i+1):
#           print(j, end=" ")
#      print()
# -----------------------------------------------------------------------------------------------
# question no:11

# for i in range(1,8):
#      for j in range(1,i+1):
#       print(i,end="")
#      print()
# -----------------------------------------------------------------------------------------------
# question no:14

# n=6
# for i in range(1,n):
#   for j in range(n,i,-1):
#     print("",end=" ")
#   for k in range(1,i+1):
#       print("*",end=" ")
#   print()
# -----------------------------------------------------------------------------------------------
  #  question no:12  
# n=6
# s=1
# for i in range(1,n):
#   for j in range(1,i):
#     print(s,end=" ")
#     s+=1
#   print()
# -----------------------------------------------------------------------------------------------
  
# question no:27
# n=int(input("Enter number"))
# for i in range(1,n):
#   result=0
#   for j in range(1,i):
#     if i%j==0:
#       result+=j
#   if i==result:
#     print("perfect number"i)
# -----------------------------------------------------------------------------------------------
  
# questionno:23
# sum=0
# x=2
# n=5
# a=1
# for i in range(1,n+1):
#   if(i%2==0):
#     sum-=x**a
#   else:
#     sum+=x**a
#   a+=2
# print("sum of series=",sum)
# -----------------------------------------------------------------------------------------------
  
# question no:24
# sum=0
# x=2
# n=5
# a=1
# for i in range(1,n+1):
#   if(i%2==0):
#     sum-=x**a
#     print(sum)
#   else:
#     sum+=x**a
#     print(sum)
#   a+=2
# print("sum of series=",sum)
  
# -----------------------------------------------------------------------------------------------
  # question no:31
# n=9
# for i in range(1,n):  
#   for j in range(n,i,-1):
#     print("",end=" ")
#   for k in range(1,i+1):
#     print("*",end=" ")
#   print()
# for i in range(1,n):
#   for k in range(i+1,0,-1):
#     print("",end=" ")
#   for j in range(i,n-1,1):
#     print("*",end=" ")
#   print()
# -----------------------------------------------------------------------------------------------
# question no:29

# n=input("enter number")
# l=len(n)
# sum=0
# for i in n:
#   sum+=int(i)**l
# if sum==int(n):
#   print("Armstron number",sum)
# else:print("Not Armstrong number",sum)
# -----------------------------------------------------------------------------------------------
  
# question no:30
# for i in range(1,1000):
#   n=i
#   l=len(str(i))
#   sum=0
#   i=str(i)
#   for j in  i:
#     sum=sum+int(j)**l
#   if(sum==n):
#    print(n)
# -----------------------------------------------------------------------------------------------
# question no:43
# n1=int(input("Enter number1 "))
# n2=int(input("Enter number2 "))
# if(n1>n2):
#   smaller=n2
# else:
#   smaller=n1
# for i in range(1,smaller+1):
#   if(n1%i==0)and(n2%i==0):
#     Hfc=i
# print("Hcf of two number",Hfc)
# -----------------------------------------------------------------------------------------------
# question no:32
# n=int(input("enter number"))
# for i in range(2,n+1):
  # if i>1 :
  #   for j in range(2,i):
  #     if(i%j==0):
  #      break
  #   else:print("prime",i)
#   else: print("Enter correct number")
# -----------------------------------------------------------------------------------------------
# question no:26
# n=int(input("enter number"))
# sum=0
# a=0
# x=10
# for i in range(1,n):
#   sum+=(x**a)
#   a+=1
# print(sum)
# -----------------------------------------------------------------------------------------------
# question no:37
# for i in range(5,0,-1):
#   print(i,end="")
# -----------------------------------------------------------------------------------------------
# question no:41
# n=int(input("Enter decimal number to Binary"))
# print(bin(n))
# -----------------------------------------------------------------------------------------------
# question no:45
# n1=int(input("Enter number1 "))
# n2=int(input("Enter number2 "))
# sum=0
# if n1>n2 :
#   smaller=n2
# else:
#   smaller=n1
# for i in range(1,smaller+1):
#   if n1%i==0 and n2%i==0 :
#     HCF=i
#     LCM=(n1*n2)/HCF
# print ("HCF of two number",HCF)  
# print ("LCM of two number",LCM)  
# -----------------------------------------------------------------------------------------------
# question no:50
# n=int(input("Enter number Decimal to octal "))
# print(oct(n))
# -----------------------------------------------------------------------------------------------
# question no:55
# n=int(input("Enter number Dceimal to Hexadecimal"))
# print(hex(79))
# -----------------------------------------------------------------------------------------------
# question no:46
# n=input("Enter number Binary to Decimal")
# s=0
# for i in n:
#   s=s*2+int(i)
# print(f"Decimal of {n} is {s}")
# -----------------------------------------------------------------------------------------------
# question no:42
# n=(input("Enter number Bibary to Decimal"))
# s=0
# for i  in n:
#   s=s*2+int(i)
# print(f"Decimal number of {n} is {s}")
# -----------------------------------------------------------------------------------------------
# question no:51
# n=input("Enter number Octal to Decimal ")
# s=0
# for i in n:
#   s=s*8+int(i)
# print(f"Decimal of {n} is {s}")
# -----------------------------------------------------------------------------------------------
# question no:59
# n=input("Enter number")
# sum=0
# l=len(n)
# for i in n:
#   sum+=int(i)**l
# if(sum==int(n)):
#   print("yes Amstrong",sum)
# else:
#   print("no Amstrong",sum)
# -----------------------------------------------------------------------------------------------
# question no:58
# w="welcome"
# l=len(w)
# print("length of string welcome is",l)
# -----------------------------------------------------------------------------------------------
