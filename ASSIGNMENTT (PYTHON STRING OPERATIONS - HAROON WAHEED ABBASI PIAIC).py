#!/usr/bin/env python
# coding: utf-8

# In[3]:


txt="my name is haroon abbasi"
x= txt.capitalize() 
print(x)


# In[16]:


txt = "HAROON ABBASI"

x = txt.casefold()

print(x)


# In[17]:


txt = "PIAIC"

x = txt.center(20) 
print(x)


# In[18]:


txt = "I love python, python is my favorite language"

x = txt.count("python")

print(x)


# In[19]:


txt = "My name is Haroon Abbasi"

x = txt.encode()

print(x)


# In[20]:


txt = "Hello, welcome to my PIAIC."

x = txt.index("PIAIC")

print(x)


# In[21]:


txt = "Hello, welcome to my PIAIC."

print(txt.find("q"))
print(txt.index("q"))


# In[22]:


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[23]:


txt = "hello world!"

x = txt.islower()

print(x)


# In[24]:


txt = "565543"

x = txt.isnumeric()

print(x)


# In[25]:


txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)


# In[26]:


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


# In[27]:


txt = "Hello my FRIENDS"

x = txt.lower()

print(x)


# In[28]:


txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)


# In[29]:


txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


# In[30]:


txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)


# In[31]:


txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")


# In[32]:


txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


# In[33]:


txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


# In[34]:


txt = "Hello My Name Is HAROON ABBASI"

x = txt.swapcase()

print(x)


# In[35]:


txt = "Welcome to my world"

x = txt.title()

print(x)


# In[36]:


txt = "Hello my friends"

x = txt.upper()

print(x)


# In[37]:


txt = "50"

x = txt.zfill(10)

print(x)


# In[ ]:




