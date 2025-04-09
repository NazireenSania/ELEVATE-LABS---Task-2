#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Step 1: Importing required libraries

import pandas as pd


# In[2]:


#checking the location of the repository

import os
print(os.getcwd())


# In[3]:


#Step 2:loading the dataset

df = pd.read_csv("sample - superstore.csv", encoding='ISO-8859-1')
df


# In[4]:


# Step 3: View basic info

print("Initial dataset shape:", df.shape)
print("\nColumn-wise missing values:\n", df.isnull().sum())


# In[5]:


#Step 4:removing duplicates

df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)


# In[7]:


df = df.dropna()
df.shape


# In[8]:


#THERE ARE NO DUPLICATES, NULL VALUES OR MISSING VALUES IN THE DATASET


# In[ ]:




