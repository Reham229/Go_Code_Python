#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Question 1

def multiply(mylist):
    result = 1
    for x in mylist:
        result = result*x
    return result                
list1= [22,33,44,55]
list2= [1,2,3,4,5]
print(multiply(list1))
print(multiply(list2))        


# In[11]:


import numpy
list1 = [22,33,44,55]
list2 = [1,2,3,4,5]

result1= numpy.prod(list1)
result2= numpy.prod(list2)

print (result1)
print(result2)


# In[12]:


x = lambda a,b,c: a*b*c
print(x(1,2,3))


# In[5]:


def my_add(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")
    return result
print(my_add(5,5))


# In[6]:


from functools import reduce
list1= [22,33,44,55]
reduce(lambda a,b: a*b, list1)


# In[7]:


from operator import mul
from functools import reduce
list1= [22,33,44,55]
reduce(mul,list1)


# In[8]:


import math
list1= [22,33,44,55]
result = math.prod(list1)
print(result)


# In[21]:


#Question 2

student_tuples = [
   ('john', 'A', 15),
   ('jane', 'B', 12),
   ('dave', 'B', 10),
 ]
sorted(student_tuples, key=lambda student: student[2])   # sort by age


# In[36]:


#Question 3

d1 = {'a': 100, 'b': 200, 'c':300,"L":400}
d2 = {'a': 300, 'b': 200, 'd':400,"e":800}
d3 = {}

for key in d1:
    if key in d2:
        d3[key]= d1[key] + d2[key]
    else:
        d3[key]= d1[key]
        
for key in d2:
    if key not in d1:
        d3[key] = d2[key]
print (d3)


# In[67]:


#Question 4

d= {}

n = 8
for i in range (1,n+1):
    d[i]= i*i
    print(d)


# In[63]:


#Question 5

list= [('item1', 12.20), ('item2', 15.10), ('item3', 24.5), ('item4', 2.5),('item5', 4.5),('item6', 0.5)]

sorted(list,key=lambda flt: flt[1], reverse= True)


# In[ ]:




