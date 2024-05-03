datas=[7,13,8,4,3,6,7,-10,-7,-12,-3,-9,-1,-6]

datas.sort()

def compute_closest_to_zero(num):
  positive=[]
  negative=[]
  for i in num:
    if i<0:
      negative.append(i)
    else:
      positive.append(i)
      positive.sort(reverse=True)
  a=positive.pop()
  b=negative.pop()
  sub=a-(-b)
  if sub>0:
    print("closed to zero",b)
  if sub==0:
    print("closed to zero",a)
  if sub<0:
    print("closed to zero",a)
compute_closest_to_zero(datas)

