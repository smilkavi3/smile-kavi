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
    

# a=142857
# c=[]
# n=6
# for i in range(1,n):
#     b=a*i
#     if (str(b) not in c) and (len(str(b))==6):
#         print("true is same digit ",b)
#     else:
#         print("false is not same digit ",b)
# print()

# a=input("enter version: ")
# b=input("enter version: ")
# n1=a.replace(".","")
# n2=b.replace(".","")
# # length1=len(n1)

# # length2=len(n2)
# # l1=[]
# # l2=[]
# # l1.append(n1)
# # l2.append(n2)
# # print(n1)
# # # sum=0
# # # sum+=a
# # if length1>length2:
# #     c.append(int(length1))
# # else:
# #     c.append(int(length2))
    
# # print(c)
# sum1=0
# for i in n1:
#     sum1=sum1+int(i)
# print()
# sum2=0
# for i in n2:
#     sum2=sum2+int(i)
#     # print(sum2)
# total=sum1-sum2
# # print(total)
# if total>0:
#     print("upgrade",a)
# if 0>total:
#     print("down grade",b)
# if 0==total:
#     print("equal",a,b)


# find the version using program:no:2
a=input("enter version: ")
b=input("enter version: ")
n1=a.replace(".","")
n2=b.replace(".","")

sum1=0
for i in n1:
    sum1=sum1+int(i)
print()
sum2=0
for i in n2:
    sum2=sum2+int(i)
    # print(sum2)
total=sum1-sum2
# print(total)
if total>0:
    print("dow grade",a)
if 0>total:
    print("up grade",b)
if 0==total:
    print("equal",a,b)