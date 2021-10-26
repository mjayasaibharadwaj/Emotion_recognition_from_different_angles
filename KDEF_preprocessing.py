#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import fnmatch
import shutil
import re
import cv2
import numpy as np
import random
from PIL import Image


# In[6]:


#source path of the KDEF dataset root folder
path = 'E:\project\datasets\KDEF_and_AKDEF\KDEF\\'
#destination folder path 
dest_path = 'E:\project\datasets\KDEF\\'


# In[8]:


all_files = []
for files in os.listdir(path):    
    for file in os.listdir(path+files):
        all_files.append(files)
        src = path + files               
        dest = "E:\project\datasets\KDEF\\"+file
        shutil.copyfile(src,dest)
print("Total files before  cleaning:", len(all_files))


# In[21]:


afraid, angry, disgust, happy, neutral, sad, surprise = ([] for i in range(7))
i,j = 4,6

#searching for the pattern in the filename

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'AF':
        afraid.append(file)
print(" afraid :", len(afraid))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'AN':
        angry.append(file)
print(" angry :", len(angry))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'DI':
        disgust.append(file)
print(" disgust :", len(disgust))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'HA':
        happy.append(file)
print(" happy :", len(happy))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'NE':
        neutral.append(file)
print(" neutral :", len(neutral))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'SA':
        sad.append(file)
print(" sad :", len(sad))

for file in os.listdir(dest_path):    
    
    if file[i : j] == 'SU':
        surprise.append(file)
print(" surprise :", len(surprise))

total = len(afraid + angry + disgust + happy + neutral + sad + surprise)
print(total)


# In[23]:


all_classes = [afraid, angry, disgust, happy, neutral, sad, surprise]
print(all_classes[6])
print(len(all_classes[6]))


# In[32]:


#moving the images to the specific emotion_classes folders

emotions_classes = ['afraid','angry','disgust','happy','neutral','sad','surprise']
# src_path = 'E:\project\datasets\jaffedbase\jfdbase\angry'

dest_path_class= 'E:\project\datasets\KDEF_class\\'
src_path = os.path.join(dest_path)
print(src_path)
for c, cls in enumerate(all_classes):
#     print(c)
    for j in cls:
        string1=str(j)
        src = src_path+string1
        if not os.path.exists(dest_path_class+emotions_classes[c]):
            os.makedirs(dest_path_class+emotions_classes[c])
        dest = dest_path_class+emotions_classes[c]+"\\"+string1
        shutil.copy2(src,dest)


# Dataset Split to train and val

# In[33]:


rootdir= 'E:\project\datasets\KDEF_class\\' #path of the original folder
val_train_folder = 'E:\project\datasets\KDEF\\'

# classes = ['disgust','fear','happy','neutral','sad','surprise','angry']

for i in emotions_classes:
    os.makedirs(val_train_folder +"\\"+'train' + "\\"+ i)

    os.makedirs(val_train_folder +"\\"+'val' + "\\"+ i)

    source = rootdir + '\\' + i

    allFileNames = os.listdir(source)

    np.random.shuffle(allFileNames)

    val_ratio = 0.20

    train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)* (1 - val_ratio))])

    train_FileNames = [source+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [source+'/' + name for name in val_FileNames.tolist()]

    for name in train_FileNames:
      shutil.copy(name, val_train_folder +"\\"+'train' + "\\"+ i)

    for name in val_FileNames:
      shutil.copy(name, val_train_folder +"\\"+'val' + "\\"+ i)

