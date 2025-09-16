#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
#      Write a python code that will generate the  the first five and last five rows of the resulting cars of the file http://bit.ly/Cars_file

# In[84]:


#importing pandas library
import pandas as pd


# In[85]:


#load the .csv file into a Dataframe named 'cars'
cars = pd.read_csv('cars.csv') 
cars


# In[86]:


#Display the first five rows of the data frame 
print("First five rows of the cars data frame: ")
cars.head()


# In[87]:


#Display the last five rows of the data frame 
print("Last five rows of the data frame: ")
cars.tail()

