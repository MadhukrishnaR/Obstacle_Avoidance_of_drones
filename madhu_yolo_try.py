#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os


# In[2]:


im0 = cv2.imread('/home/nano/Desktop/left2/frame0078.jpg')
#im1 = plt.imread('frame0120.jpg')


# In[3]:


bbox0, label0, conf0 = cv.detect_common_objects(im0)
#bbox1, label1, conf1 = cv.detect_common_objects(im1)


# In[4]:


output_image0 = draw_bbox(im0, bbox0, label0, conf0)
#output_image1 = draw_bbox(im1, bbox1, label1, conf1)


# In[5]:


#bbox0


# In[6]:


#x0 = int((bbox0[0][0]+bbox0[0][2])/2)
#y0 = int((bbox0[0][1]+bbox0[0][3])/2)


# In[7]:


print(bbox0)


# In[8]:


#x1 = int((bbox1[0][0]+bbox1[0][2])/2)
#y1 = int((bbox1[0][1]+bbox1[0][3])/2)


# In[9]:


cv2.imshow("Output", output_image0)
cv2.waitKey(0)
cv2.destroyAllWindows()
