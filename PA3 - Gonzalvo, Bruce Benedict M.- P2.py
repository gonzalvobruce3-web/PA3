#!/usr/bin/env python
# coding: utf-8

# ## Problem 2
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

# In[41]:


#importing pandas library
import pandas as pd 


# In[42]:


#load the .csv file into a Dataframe named 'cars'
cars = pd.read_csv('cars.csv') 
cars


# In[43]:


#Display the first five rows with odd-numbered columns (1-indexed)
#the first five rows with odd numbered columns are 'Model', 'cyl', 'hp', 'wt', 'vs', and 'gear'. 
odd_columns = cars.iloc[:, [i for i in range (cars.shape[1]) if i%2 == 0]]
print("First Five rows with odd-numbered columns")
odd_columns.head()


# In[63]:


#Display the row that contains the ‘Model’ of ‘Mazda RX4’
mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
print("Row for the model 'Mazda RX4':")
mazda_rx4_row


# In[61]:


#Display the numbers of cylinders('cyl') for'Camora Z28: 8'
print("\nNumber of cylinders for 'Camaro Z28':")
cars.loc[[23],['Model', 'cyl']]


# In[17]:


#Display the cylinders('cyl') and gear type('gear') of models Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’
models_info = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['Model', 'cyl', 'gear']]
print("cylinders and gear type for specified models")
models_info

