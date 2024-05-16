
# question no:13
# pyramid pattern with number increased by 1:
# n=5
# s=1
# for i in range(1,n):
#     for j in range(n,i,-1):
#         print("",end=" ")
#     for k in range(1,i+1):
#         print(s,end=" ")
#         s=s+1
#     print()
# -----------------------------------------------------------------------------
# question no:17
# Reoeat the number in the same row:
# n=5
# for i in range(1,n):
#     for j in range(n,i,-1):
#         print("",end=" ")
#     for k in range(i,0,-1):
#         print(i,end=" ")
#     print()
# for i in range(0,5):
#     for j in range(i+1,):
#        print((j+1)%2,end="")
#     print()
# -----------------------------------------------------------------------------
# To find sum of even number:
# a=1
# n=6
# sum=0
# for i in range (1,n):
#    sum=sum+(1/a)
#    a+=1
# print("sum is ",sum)

# sum=0
# for i in range(2,11,2):
#     sum=sum+i
#     print(f"even {i}")
# print("sum of even number=",sum)

# -----------------------------------------------------------------------------
# question no:25
# To find the Squar of natural number:
# a=1
# sum=0
# for i in range(1,6):
#     sum=sum+a**2
#     a+=1
# print("square of Natural number=",sum)
# -----------------------------------------------------------------------------
# question no:15
# To find Factorial of number:
# n=int(input("Enter number to find factorial"))
# s=1
# for i in range(1,n+1):
#     s=s*i
#     # print(s) (it option)
# print(f"Factorial of {n}",s)
# -----------------------------------------------------------------------------
# question no:35
# n=int(input("Enter number"))
# f=0
# s=1
# for i in range(0,n+1):
#     print(f)
#     k=f
#     f=s
#     s=k+s
# -----------------------------------------------------------------------------
# question no:57
# n="welcome"
# l=len(n)
# for i in range(-1,-l,-1):      
#     print(n[i],end=" ")
# -----------------------------------------------------------------------------
# question no:49
# n=int(input("Enter number of series "))
# s=0
# a=1
# for i in range(1,n+1):
#     s=s+a
#     a+=4
# print(s)
# -----------------------------------------------------------------------------
# question no:47
# To find the Strong number:
# n=input("Enter number")
# s=0
# for i in n:
#     i=int(i)
#     f=1
#     for j in range(1,i+1):
#      f=f*j
#     s=s+f  
# if (int(n)==s):
#     print("Strong number",n)
# else:print("Not strong number",n)
# -----------------------------------------------------------------------------
# question no:54
# To convert octal to binary conversion:
# n=input("Enter octal number  ")
# s=0
# for i in n:
#     s=s*8+int(i)
# b=bin(s)
# print(f" octal to binary coversion:",b)
# -----------------------------------------------------------------------------
# question no:55
# To convert the decimal to hexa decimal number:
# n=input("Enter deimal number: ")
# s=0
# for i in n:
#     s=s*10+int(i)
# h=hex(s)
# print("Decimal to Hexa decimal conversion: ",h)
# -----------------------------------------------------------------------------
# question no:53
# To convert the binary to octal number:
# n=input("Enter binary number:")
# s=0
# for i in n:
#     s=s*2+int(i)
# o=oct(s)
# print("Binary to octal conversion: ",o)
# -----------------------------------------------------------------------------
# find prime number:
# n=int(input("Enterr number"))
# if n>1:
#  for i in range(2,n):
#   if n%i==0:
#     print("Not prime",n)
#     break
#   else:
#     print("prime",n)


