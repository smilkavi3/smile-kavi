# flams game using program :no:1
# name1=input("Enter name:").lower()
# name2=input("Enter name:").lower()

# def function():
#  name1=input("Enter name:").lower()
#  name2=input("Enter name:").lower()
#  name1=name1.replace(" ","")
#  name2=name2.replace(" ","")
#  for i in name1:
#     for j in name2:
#         if i==j:
#             name1=name1.replace(i,"",1)
#             name2=name2.replace(j,"",1)
#             break  
        
                         
#  count=len(name1+name2)
# #  print(count)
#  if count>0:
#     list=["f","l","a","m","e","s"]
#     while len(list)>1:
#       c=count%len(list)
#       index=c-1
#       if index>=0:
#          left=list[:index]
#          right=list[index+1:]
#          list=right+left
#       else:
#          list=list[:len(list)-1]
#     print("relation  is: ",list[0])
#  else:
#     print("different")
# function()
    

# find the version using program:no:2
# def version():
#  a=input("enter version 1: ")
#  b=input("enter version 2: ")
#  n1=a.replace(".","")
#  n2=b.replace(".","")
#  length1=len(n1)
#  length2=len(n2)
#  l1=[]
#  l2=[]
#  sum1=0
#  for i in n1:
#     l1.append(i)
#     sum1=sum1+int(i)

#  sum2=0
#  for i in n2:
#     l2.append(i)
#     sum2=sum2+int(i)
    
#  total=sum2-sum1
#  c=l1[0]
#  d=l2[0]
#  if length1==length2:
#   if length1==2 and length2==2:  
#     if d>c:
#       print("up grade",b)
#     else:
#         print("down",b)
#   elif  total>0:
#     print("up grade",b)
#   elif  0<total:
#     print("up grade ",b)
#   elif total==0:
#     print("equal",a,b)
#   else:
#     print("down grade",b)
#  elif c>d:
#     print("down grade",b)   
#  elif c<d:
#     print("up grade",b)
#  elif sum1==sum2:
#     print("eqyal",b)
#  else:
#     print("down grade",b)
# version()

# owner_player={}
# while True:
#    owner= input("enterr owner name(or type done to finish): ")
#    if owner =="done":
#       break
#    player= input("enterr player name: ")
#    owner_player[owner]=player
# print(owner_player)

# n=60
# deg=[0,30,0,-45,0]
# l=[]
# for i in deg:
#    if i==0 :
#       l.append(n)
#    elif i<0:
#       n-=i
#       l.append(n)
#    elif i>0:
#       n-=i
#       l.append(n)
# print(l)

# missing number count:qn:1
# l=[0,10,5,8,7]
# def missing_num(a):
#     n=int(input("enter the maximum range: "))
#     length=len(a)
#     missing_count=(n+1)-length
#     return missing_count
# b=missing_num(l)
# print(b)

# Roman number:
# roman_num={
#     "V":5,
#     "VI":6,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000,
#     "X":10
# }
# n=input("Enter the num: ")
# a=n.upper()
# for i in a:
#     c=roman_num[i]
# print(f"roman_num {n}-{c}")

# sum of two array in given value:
array=[1,4,45,6,10,8]
length=len(array)
for i in range(length):
    for j in range(i+1,length):
        if array[i]+array[j]==16:
            print(f"sum of array[{i}] + array[{j}]==16")


