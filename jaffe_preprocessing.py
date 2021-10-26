#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import fnmatch
import shutil
import re
import numpy as np
import random


# In[4]:


path = 'E:\project\datasets\jaffedbase\jaffedbase'
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)


# In[6]:


angry, disgust , fear , happy, neutral, sad, surprise = ([] for i in range(7))
for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*DI*.tiff'):
        
        disgust.append(files)
print(" disgust :", len(disgust))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*FE*.tiff'):
        
        fear.append(files)
print(" fear :", len(fear))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*HA*.tiff'):
        
        happy.append(files)
print(" happy :", len(happy))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*NE*.tiff'):
        
        neutral.append(files)
print(" neutral :", len(neutral))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*SA*.tiff'):
        
        sad.append(files)
print(" sad :", len(sad))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*SU*.tiff'):
        
        surprise.append(files)
print(" surprise :", len(surprise))

for files in os.listdir(path):
    
    if fnmatch.fnmatch(files, '*AN*.tiff'):
        
        angry.append(files)
print(" angry :", len(angry))

total = len(angry + sad + happy + surprise + disgust + fear + neutral)
print(total)


# In[7]:


all_classes = [disgust, fear, happy, neutral, sad, surprise, angry]
print(all_classes[6])


# In[142]:


# emotions = ['AN', 'DI', 'FE', 'HA', 'NE', 'SA', 'SU']
# angry = []
# src_path = 'E:\project\datasets\jaffedbase\jfdbase\angry'
# path = 'E:\project\datasets\jaffedbase\jaffedbase'
# angry = []
# dest_path= 'E:\project\datasets\jaffedbase\jfdbase\\'

# for files in os.listdir(path):
#     if fnmatch.fnmatch(files, '*AN*.tiff'):
# #         print(files) # for checking
#         angry.append(files)
#         for j in angry:
#             string1=str(j)
#             src = path+"\\"+string1
#             if not os.path.exists(dest_path+"angry"):
#                 os.makedirs(dest_path+"angry")
#             dest = dest_path+"angry"
#             shutil.copy2(src,dest)


# In[9]:


emotions_classes = ['disgust','fear','happy','neutral','sad','surprise','angry']
# src_path = 'E:\project\datasets\jaffedbase\jfdbase\angry'
path = 'E:\project\datasets\jaffedbase\jaffedbase'
dest_path= 'E:\project\datasets\jaffedbase\jfdbase\\'

for c, cls in enumerate(all_classes):
    print(cls)
    for j in cls:
        string1=str(j)
        src = path+"\\"+string1
        if not os.path.exists(dest_path+emotions_classes[c]):
            os.makedirs(dest_path+emotions_classes[c])
        dest = dest_path+emotions_classes[c]
        shutil.copy2(src,dest)


# In[143]:


# for c, e in enumerate(emotions_classes):
#     print(c, e)


# In[12]:


emotions_classes[0]


# Dataset Split to train and val

# In[13]:


rootdir= 'E:\project\datasets\jaffedbase\jfdbase\\' #path of the original folder

classes = ['disgust','fear','happy','neutral','sad','surprise','angry']

for i in classes:
    os.makedirs(rootdir +"\\"+'train' + "\\"+ i)

    os.makedirs(rootdir +"\\"+'val' + "\\"+ i)

    source = rootdir + '\\' + i

    allFileNames = os.listdir(source)

    np.random.shuffle(allFileNames)

    val_ratio = 0.20

    train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)* (1 - val_ratio))])

    train_FileNames = [source+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [source+'/' + name for name in val_FileNames.tolist()]

    for name in train_FileNames:
      shutil.copy(name, rootdir +"\\"+'train' + "\\"+ i)

    for name in val_FileNames:
      shutil.copy(name, rootdir +"\\"+'val' + "\\"+ i)

