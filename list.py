# print alternate index of the list:1
# l=[1,2,3,4,5]
# r=l[::2]
# print(r)

# sum of list number:2
# l=[1,2,3,4,5]
# l1=len(l)
# s=0
# for i in range(l1):
#     s=s+l[i]
# print(s)

# print the index of given number: using loop:3
# l=[10,44,63,44,3,5,44]
# n=44
# l1=len(l)
# for i in range(l1):
#   value=l[i]
#   if value==44:
#     print(i,end=" ")

        
# Print the list:4    
# l=[1,2,3,4,5]
# print(l)

# print the perfect list:5
# l=[1,2,3,2,1]
# if l[::1]==l[::-1]:
#   print("perfect",l)
# else:print("not perfect",l)


# swap two number in given list:6
# l=[12,36,48,60]
# a=l[0]
# l[0]=l[-1]
# l[-1]=a
# print(l)


# Remove the duplicate file:7
# l=[12,36,12,60,1,86,99,23,1,3,7,2,99,2]
# orginal=[]
# for i in l:
#     if i not in orginal:
#         orginal.append(i)
# print(sorted(orginal))


# Find larger and smaller number:8
# l=[1, 2, 8, 10, 11, 12, 19]
# n=5
# greater=0
# minimum=0
# for i in l:
#     if i<=n:
#         greater+=1
#     else:
#         minimum+=1
# print(greater)
# print(minimum)

# Delet the largest two number:9
# l=[7, -2, 3, 4, 9, -1]
# l1=[]
# for i in l:
#     if i<max(l):
#         l1.append(i)
#         sort=sorted(l1)
# print("Sorted:",sort)
# print("Delet the last greater number:",sort.pop())
# print("After Delet new list:",sort)

# Count smaller elements:10
# l=[1, 2, 2, 2, 5, 7, 9]
# l1=[]
# c=0
# n=int(input("Enter number:"))
# for i in l:
#     if i<=n:
#         l1.append(i)
#         sort=sorted(l1)
#         c+=1
# print("Sorted list:",sort) 
# print("Count value of small elements:",c) 

# Find value equal to list of index value:11
# l=[15, 2, 45, 3, 7]
# l1=len(l)
# for i in range(l1):
#      a=l[i]
#      if i==a:
#          print("Value of list",l[i]) 


# Print the left element of given list:12
# l=[8, 1, 2, 9, 4, 3, 7, 5]
# a=sorted(l)
# length=len(l)//2
# print(a)
# print("Midle of list element:",length)
# print("The last number of list is:",a[length-1])

# compare the list of a,b and increse the count:13
# a=[4, 2, 7]
# b=[5, 6, 3]
# length=len(a)
# ca=cb=0
# for i in range (length) :
#     if a[i]>b[i]:
#         ca+=1
#     elif a[i]<b[i]:
#         cb+=1      
# print("count of a:",ca)
# print("count of b:",cb)

# l=192
# l1=[]
# a=l*2
# l1.append(a)
# b=l*3
# l1.append(b)
# l1.append(l)
# print(l1)

# person=[
#    {
#    "Name":"gowtham",
#    "age": 18,
#    "state":"tamil nadu",  
#    },
#       {"Name":"asoon",
#    "age": 17,
#    "state":"tamil nadu",
#    }
#       ]
# new=[]
# for i in person:
#    a=i["age"]
#    print(a)
#    if a<=18:
#       j=0
#       person[i]["age"]
#       print(person)
   