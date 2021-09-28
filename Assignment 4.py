#!/usr/bin/env python
# coding: utf-8

# In[15]:


r = lambda a : a+25
print(r(10))


# In[18]:


x = [1, 2, 3, 4, 5, 6, 7]
y = map(lambda a : a+a+a , x)
print(list(y))


# In[19]:


list(map(lambda x : x**2 , [4, 5, 2, 9]))

