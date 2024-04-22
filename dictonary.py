
# topic is DICTONARY: 
# finding vote eligible in given dictonary:
# person=[
#    {
#    "Name":"gowtham",
#    "age": 18,
#    "state":"tamil nadu",  
#    },
#       {"Name":"asoon",
#    "age": 15,
#    "state":"tamil nadu",
#    }
#       ]
# for i in person:
#    a=i["age"]
#    if i["age"]>=18:
#       print(" Eligible",a)
#    else:
#       print(" Not Eligible",a)

# question no:02
# Write a python script to add a key to a dictonary:
# sampledictionary={0:10,1:20}
# sampledictionary[4]=30
# print(sampledictionary)

# question no:03
# # to create the new dictonary:
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dict={}
# dict=dic1.copy()
# dict.update(dic2)
# dict.update(dic3)
# print(dict)

# question no:4
# To check wheather a given key already exists in a dictonary:
# dict={1:10,2:20,3:30,4:40,5:50,6:60}
# n=int(input("Enter key"))
# if n in dict:
#     print("Already exist")
# else:
#     print("not exist")

# question no:6,7
# Write a python script to print a dictionary where the keys are number berween 1 and 15
# the values are the square of keys
# num=int(input("Enter the number:"))
# dic={}
# for i in range(1,num+1):
#     dic[i]=i*i
# print(dic)

# question no:15
# write a python program to find maximum and minimum number a dictionary:
# dic={1:10,2:20,3:30,4:40,5:50,6:60}
# a=min(dic.items())
# b=max(dic.items())
# print("Maximum number in a dictionary",b)
# print("Minimum number in a dictionary",a)


# python program to remove a key from a dictonary:
# dic={1:10,2:20,3:30,4:40,5:50,6:60}
# key=int(input("enter keys:"))
# dict.pop(key)
# print(dic)

# question no:10
# sum of all the items in a dictionary:
# dic={1:10,2:20,3:30,4:40,5:50,6:60}
# sum=0
# sum1=0
# for k in dic:
#   sum+=dic[k]
#   sum1+=k
# print("sum of dictionary value:",sum)
# print("sum of dictionary keys:",sum1)


# sort(Ascending and descending) a dictionary by value 
# dic={5:10,2:20,6:30,4:40,3:5,1:60}
# c=[]
# d=[]
# a=sorted(dic.values())
# print("sort the values:",a)   
# for i in dic:
#     a=dic[i]
#     c.append(a)
#     d.append(i)
# c.sort(reverse=True)
# d.sort()
# print("reverse the dictionary values:",c)
# print("sort the dictionary keys:",d)

# Convert to list into dictionary:
# l1=[1,2,3,4,5,6]
# l2=[20,30,40,50,60,70]
# length=len(l1)
# c={}
# for i in range(length):
#    c[l1[i]]=l2[i] 
# print(c)

# question no:19
# Combine two dictionary by adding values for common keys:
# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# for i in d2:
#     if i in d1:
#         d1[i]+=d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)

# To remove the given string and add the given dictonary:
# t="geekforgeeks best for "
# r={"geeks":"all cs aspirants"}
# a=t.split()
# a.pop()
# list=[]
# list=a
# list.append(r["geeks"])
# for i in list:
#    print(i,end=" ")

# remove duplicate files:
# dic={"a":100,"b":201,"c":300,"a":200,"d":250}
# d2={}
# d3={}
# for k,v in dic.items():
#     if k  not in d2.keys():
#        d2[k]=v
#     else:
#         d3[k]=v
# print(d2)
# print(d3)

#Rotate the list:
# l=[-1,-2,-3,4,5,6,7]
# l=[1,3,4,2]
# for i in range(0,2):
#     a=l[len(l)-1]
#     # print(a)
#     for j in range(len(l)-1,0,-1):
#       l[j]=l[j-1]
#     l[0]=a
# print(l)

# l=[1,3,4,2]
# l1=len(l)
# for i in range(l1):
#     a=i,l[i]
#     # print(a)
#     b=(i+3)//l1
#     l[b]=l[i]
#     print(l)

# paranthissis program:
# l="[(])"
# l1=[]
# l2=[]
# le=len(l)
# count=0
# for i in range(le):
#     a=l[i]
#     if a=="{"or a=="["or a=="(":
#         # l1.append(a) 
#         count+=1
#     elif a=="}"or a=="]"or a==")":
#         # l2.append(a)
#         count-=1
# # print(count)
# if count==0:
#     print("true",count)
# else:
#     print("false",count)

  