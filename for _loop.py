
n=5
for i in range(1,n):
    for j in range(n,i,-1):
        print("",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
        k+=1
    print()
 
for i in range(0,5):
    for j in range(i+1,):
       print((j+1)%2,end="")
    print()


a=1
n=6
sum=0
for i in range (1,n):
   sum=sum+(1/a)
   a+=1
print("sum is ",sum)

sum=0
for i in range(2,11,2):
    sum=sum+i
    print(f"even {i}")
print("sum of even number=",sum)


a=1
sum=0
for i in range(1,6):
    sum=sum+a**2
    a+=1
print("square of Natural number=",sum)



