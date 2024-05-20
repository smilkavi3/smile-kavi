# flams game:
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
    

a=142857
c=[]
n=6
for i in range(1,n):
    b=a*i
    if (str(b) not in c) and (len(str(b))==6):
        print("true is same digit ",b)
    else:
        print("false is not same digit ",b)
print()