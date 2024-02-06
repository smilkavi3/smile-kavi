
n=5
# for i in range(1,n):
#     for j in range(n,i,-1):
#         print("",end=" ")
#     for k in range(i,0,-1):
#         print(k,end=" ")
#         k+=1
#     print()
 
# for i in range(0,5):
#     for j in range(i+1,):
#        print((j+1)%2,end="")
#     print()
# a=float(input("enter number"))
# x=float(input("enter number"))

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

# a=10
# sum=0
# for i in range (1,6):
#    sum=sum+a-1
#    a*=10
# print("sum=",sum)

# a=1
# sum=0
# for i in range(1,6):
#     sum=sum+a**2
#     a+=1
# print("square of Natural number=",sum)

sum=0
n=int(input("Enter number"))
for i in range(1,n):
    if(n%i==0):
      sum=sum+i
      print(f" {i}",end="")
      print()
print("Sum of divisor is=",sum)
if(sum==n):
   print("Perfect divisor")
else:
   print("Not perfect divisor")


