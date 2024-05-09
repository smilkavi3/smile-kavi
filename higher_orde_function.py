# higher order function is input a function and output a function

# lamda function: is anonimes function and it performs single line operation:
x=lambda a,b:a+b
print(x(3,4))

# map function:
#  function must have two function:
# it gives equal length of given list and perform arithmetic operation
l=[1,2,3,4]
print(list(map(lambda i:i*2,l)))

# reduce function:
# it gives single value and import functools in normal operation and import operator in arithmetic operation
import functools
import operator
l=[-2,7,123,-150,270]
print(functools.reduce(lambda a,b: a if a<b else b ,l))

# only perform add,sub,multiply,division:
l=[1,2,3,4]
print(functools.reduce(operator.add,l))

# filter function
# using condiction operation and given codition true and print the number
l=[1,2,3,4,5]
print(list(filter(lambda a:(a+1)%3==0,l)))


