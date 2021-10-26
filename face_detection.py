#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
import cv2
import numpy as np


# In[13]:


#import model paths

dataset_dir = os.path.join("/home/home02/sc20jbm/project/KDEF/")
prototxt_path = os.path.join('model_data/deploy.prototxt')
caffemodel_path = os.path.join('model_data/weights.caffemodel')


# In[14]:


dataset_dir


# In[15]:


model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)


# In[16]:


if not os.path.exists('faces'):
	print("New directory created")
	os.makedirs('faces')


# In[11]:


count = 0
for dataset_name in os.listdir(dataset_dir):
# 	print(dataset_name)
	for class_name in os.listdir(dataset_dir + '/' + dataset_name):
# 		print(class_name)
		for file in os.listdir(dataset_dir + '/' + dataset_name  + '/' +  class_name):
			# print(file)
			file_name, file_extension = os.path.splitext(file)
			if (file_extension in  ['.jpg','.JPG', '.tiff']):
				path = os.path.join(dataset_dir + '/' + dataset_name + '/' +  class_name +  '/' +  file)
# 				print(path)
				image = cv2.imread(path)
				# print(image)
				(h, w) = image.shape[:2]
				width = 224
				height = image.shape[0]
				dim = (width, height)
				blob = cv2.dnn.blobFromImage(cv2.resize(image, dim, interpolation = cv2.INTER_AREA ), 1.0, dim , (104.0, 177.0, 123.0))

				model.setInput(blob)
				detections = model.forward()

				# Identify each face
				for i in range(0, detections.shape[1]):
					box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
					(startX, startY, endX, endY) = box.astype("int")

					confidence = detections[0, 0, i, 2]

					# If confidence > 0.5, save it as a separate file
					if (confidence > 0.5):
						count += 1
						frame = image[startY:endY, startX:endX]
						cv2.imwrite('faces3/' + file, frame)

print("Extracted " + str(count) + " faces from all images")


# In[ ]:


c_files = []
resized_f = []
for count, cr_file in enumerate(os.listdir(source_path)):
    c_files.append(cr_file)

    image_cr = cv2.imread(os.path.join(source_path + c_files[count]))
#     print(image_cr.shape)
    width = 224
    height = 224
    dim = (width,height)
    resized = cv2.resize(image_cr, dim, interpolation = cv2.INTER_AREA)
    resized_f.append(resized)
    imageRGB = cv2.cvtColor(resized_f[count], cv2.COLOR_BGR2RGB)
    image_cr = Image.fromarray(imageRGB)
    string2=str(c_files[count])
    image_cr.save(destination_cr_path + string2 )
    

