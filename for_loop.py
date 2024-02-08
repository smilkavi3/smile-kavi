# for i in range(1,11):
#     print(i)

# for i in range(1,11):
#     print(i)
s=0
# for i in range(1,11):
#     s+=i

# print("sum",s)


# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n):
#     print(i)
#     s1=s1+i

# print("sum",s1)


# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n):
#      print(i)
#      s1=s1+i

#      s=s1/10

# print("sum",s1)
# print("average",s)


# n=int(input("Enter numbers"))
# for i in range(1,5,1):
#  cubeValue=i ** 3
#  print(f"number is {i} and cube value {i} is",cubeValue)

# n=int(input("Enter numbers"))
# s1=0
# for i in range(1,n,1):
#  if(i%2!=0):
#   print(i,"odd")
#   s1+=i
# print("sum",s1) 
 
# s=15
# for i in range(1,11,1):
#  multiplication=s*i
#  print(f"{s}x{i}",multiplication)

s1=1
s2=2
s3=3
s4=4
s5=5
s6=6
s7=7
s8=8
s9=9
s10=10

# t = 0
# m = 1

# for i in range(1,80):
#     #   t += 1
#       pri#   t += 1
#       print(f"{m} x {t} = {m * t}")
#       if(t % 10 == 0):
#             t = 0
#             m += 1
#             print()


# for i in range(1,51):
#       for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
#       print()
      


# for i in range(1,11):
#       m1=s1*i
#       print(f"{i}x{s1}",m1)


# for i in range(1,11):
#     m2=s2*i
#     print(f"{i}x{s2}",m2)


# for i in range(1,11):
#     m3=s3*i
#     print(f"{i}x{s3}",m3)

# a="*"
# for i in range(1,6):
#      print(a*i)



# for i in range(1,2):
#   print(i)
#   for m in range(2,3):
#     print(i,m)
#     for j in range(3,4):
#       print(i,m,j)
#       for l in range(4,5):
#         print(i,m,j,l)

# rowCountEnd = 1
# inc = 0
# logic = 0+1,1+2,3+3,6+4,10+5,

# for i in range(10):
#      inc += 1
#      print(inc, end = " ")
#      if(rowCountEnd == inc):
#           rowCountEnd += 1
#           inc = 0
#           print()

     
# for i in range(1,11):
#      for j in range(1,i+1):
#           print(j, end=" ")
#      print()

# for i in range(1,8):
#      for j in range(1,i+1):
#       print(i,end="")
#      print()
# n=6
# for i in range(1,n):
#   for j in range(n,i,-1):
#     print("",end=" ")
#   for k in range(1,i+1):
#       print("*",end=" ")
#   print()
     
# for i in range(1,n):
#   for j in range(i,0,-1):
#     print(i,end="")
#     i+=1
#   print()
  
# question no:27
# n=int(input("Enter number"))
# sum=0
# for i in range(1,n):
#   if(n%i==0):
#     sum+=i
#     print(f"{i}",end="")
#     print()
# print("sum of divisor is",sum)
# if(n==sum):
#   print("perfect")
# else:
#   print("Not perfect")  
  
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
  
  # question no:31
n=9
for i in range(1,n):
  for j in range(n,i,-1):
    print("",end=" ")
  for k in range(1,i+1):
    print("*",end=" ")
  print()
n= 9 
for i in range(1,n):
  for k in range(1,i+1):
    print("",end=" ")
  for j in range(i,n,1):
    print("*",end=" ")
  print()