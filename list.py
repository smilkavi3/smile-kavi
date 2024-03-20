# print alternate index of the list:
# l=[1,2,3,4,5]
# r=l[::2]
# print(r)

# sum of list number:
# l=[1,2,3,4,5]
# l1=len(l)
# s=0
# for i in range(l1):
#     s=s+l[i]
# print(s)

# print the index of given number: using loop
# l=[10,44,63,44,3,5,44]
# n=44
# l1=len(l)
# for i in range(l1):
#   value=l[i]
#   if value==44:
#     print(i,end=" ")

        
# Print the list:     
# l=[1,2,3,4,5]
# print(l)

# print the perfect list:
# l=[1,2,3,2,1]
# if l[::1]==l[::-1]:
#   print("perfect",l)
# else:print("not perfect",l)


# swap two number in given list:
# l=[12,36,48,60]
# a=l[0]
# l[0]=l[-1]
# l[-1]=a
# print(l)


# Remove the duplicate file:
# l=[12,36,12,60,1,86,99,23,1,3,7,2,99,2]
# orginal=[]
# for i in l:
#     if i not in orginal:
#         orginal.append(i)
# print(sorted(orginal))


# Find larger and smaller number:
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

# Delet the largest two number:
# l=[7, -2, 3, 4, 9, -1]
# l1=[]
# for i in l:
#     if i<max(l):
#         l1.append(i)
#         sort=sorted(l1)
# print("Sorted:",sort)
# print("Delet the last greater number:",sort.pop())
# print("After Delet new list:",sort)

# Count smaller elements:
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

# Find value equal to index value:
l=[15, 2, 45, 3, 7]
l1=len(l)
for i in range(l1):
     a=l[i]
     if i==a:
         print("Value of list",l[i]) 
