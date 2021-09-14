#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a python program to implement your own myreduce() function which works exactly like pyhton's builtin function reduce().
G = [1,2,3,4,5]
from functools import reduce
reduce(lambda a,b:a*b,G)


# In[3]:


def muli(a,b):
    return a*b


# In[4]:


reduce(muli,G)


# In[7]:


M = [1,2,3,4,5,"gaurav"]
reduce(lambda a,b: a if type(a) == str else b,M)


# In[16]:


def test(a,b):
    if type(a) == str:
        return a
    else:
        return b


# In[18]:


reduce(test,M)


# In[20]:


#Write a python program to implement your own myfilter() function which works exactly like pyhton's builtin function filter().
X = [4,5,6,7,8,"Jagtap"]
list(filter(lambda a: True if type(a) == str else False,X))


# In[29]:


L = [1,2,6,5,55,88,-2,0]
def test1(n):
    if (n) >= 5:
        return True
    else:
        False


# In[30]:


list(filter(test1,L))


# In[35]:


#Implement list comprehension to produce the following lists
#2.1 ['x','xx','xxx','xxxx','y','yy','yyy','yyyy','z','zz','zzz','zzzz']
list = ['x','y','z']
result = [i*num for i in list for num in range(1,5)]
print(str(result))


# In[36]:


#2.2 ['x','y','z','xx','yy','zz','xxx','yyy','zzz','xxxx','yyyy','zzzz']
list2 = ['x','y','z']
result = [i*num for num in range(1,5) for i in list2]
print(str(result))


# In[49]:


#2.3[[2],[3],[4],[3],[4],[5],[4],[5],[6]][[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
list3 = [2,3,4]
list4 = [2,3,4,5]
result3 = [[i+num] for i in list3 for num in range(0,3)]
result4 = [[i+num for i in list4] for num in range(0,4)]
print(str(result3),(result4))


# In[52]:


#2.4[(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3)]
list5 = [1,2,3]
result = [(b,a) for a in list5 for b in list5]
print(str(result))


# In[ ]:





# In[ ]:




