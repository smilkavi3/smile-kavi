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
a=input("enter version 1: ")
b=input("enter version 2: ")
n1=a.replace(".","")
n2=b.replace(".","")
length1=len(n1)
length2=len(n2)
l1=[]
l2=[]
sum1=0
for i in n1:
    l1.append(i)
    sum1=sum1+int(i)
print()
sum2=0
for i in n2:
    l2.append(i)
    sum2=sum2+int(i)
    
total=sum2-sum1
c=l1[0]
d=l2[0]
if length1==length2:
 if  total<0:
    print("down grade",b)
 elif  0<total:
    print("up grade ",b)
 elif total==0:
    print("equal",a,b)
 else:
    print("down grade",b)
elif c>d:
    print("down grade",b)   
elif c<d:
    print("up grade",b)
elif sum1==sum2:
    print("eqyal",b)
else:
    print("down grade",b)