#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[86]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from skimage import io
from skimage import exposure


#  Study area is selected as Burdur/Turkey to see the amount of lakes and the vegetation near the lakes in two years: 1985 and 2020. Autumn is selected as the season for both years so, september, october and november are selected as the study months.

# # Importing the Data from Landsat TM 5 and Generating the Bands

# In[87]:


image1 = io.imread('C:/Users/asus/Downloads/LT05_L1TP_178034_19850921_20200918_02_T1_B1.TIF')
image2 = io.imread('C:/Users/asus/Downloads/LT05_L1TP_178034_19850921_20200918_02_T1_B2.TIF')
image3 = io.imread('C:/Users/asus/Downloads/LT05_L1TP_178034_19850921_20200918_02_T1_B3.TIF')
image4 = io.imread('C:/Users/asus/Downloads/LT05_L1TP_178034_19850921_20200918_02_T1_B4.TIF')


# In[88]:


B1 = np.array(image1).astype(float)
B2 = np.array(image2).astype(float)
B3 = np.array(image3).astype(float)
B4 = np.array(image4).astype(float)


# In[89]:


blue = (B1-np.min(B1))/(np.max(B1)-np.min(B1))
green = (B2-np.min(B2))/(np.max(B2)-np.min(B2))
red = (B3-np.min(B3))/(np.max(B3)-np.min(B3))
nir = (B4-np.min(B4))/(np.max(B4)-np.min(B4))


# # NDVI Calculation for 1985 Image

# In[90]:


#NDVI
NDVI = (nir-red)/(nir+red)


# In[115]:


plt.figure(figsize=(15,10))
plt.imshow(NDVI, cmap=cm.Greys)
plt.title('NDVI Image')
plt.colorbar()
plt.axis('off')
plt.show()


# In[92]:


NDVI1 = io.imsave(fname="NDVI.tif", arr=NDVI)


# In[93]:



rgb = np.stack([nir, red, green], axis=2)
threshold = 0.2
veg = NDVI > threshold
non_veg = NDVI <= threshold


# In[94]:


fig , ax = plt.subplots(nrows=2, ncols=2, figsize=(15,15))
ax[0,0].imshow(rgb)
ax[0,0].set_title('RGB Image')
ax[0,0].axis('off')
######
ax[0,1].imshow(NDVI, cmap=cm.Greens)
ax[0,1].set_title('NDVI-Image')
ax[0,1].axis('off')
######
ax[1,0].imshow(veg, cmap=cm.Greens)
ax[1,0].set_title('Vegetation-Area')
ax[1,0].axis('off')
######
ax[1,1].imshow(non_veg, cmap=cm.Blues)
ax[1,1].set_title('Non-Vegetation Area')
ax[1,1].axis('off')
plt.show()


# In the images given above, Vegetaion-Area image shows the areas vegetated with green color while Non-Vegetation Area image shows the non-vegetated areas with blue.

# # NDWI Calculation for 1985 Image

# In[95]:


#NDWI
NDWI = (green - nir)/(green + nir)


# In[96]:


plt.figure(figsize=(15,10))
plt.imshow(NDWI, cmap=cm.gray)
plt.title('NDWI Image')
plt.colorbar()
plt.axis('off')
plt.show()


# In[97]:


NDWI1 = io.imsave(fname="NDWI.tif", arr=NDWI)


# In[98]:


rgb = np.stack([nir, red, green], axis=2)
threshold = 0.05
water1 = NDWI > threshold
non_wat1 = NDWI <= threshold


# In[99]:


fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(15,15))

######
ax[0].imshow(water1, cmap=cm.Greens)
ax[0].set_title('Water-Area')
ax[0].axis('off')
######
ax[1].imshow(non_wat1, cmap=cm.Reds)
ax[1].set_title('Non-Water Area')
ax[1].axis('off')
plt.show()


# In the two images given above, green colors indicates the water areas in 1985. As a different way to show is the red areas indicates the areas without water.

# # Importing Landsat 8 Data and Generating Bands

# In[100]:


image1 = io.imread('C:/Users/asus/Downloads/LC08_L1TP_178034_20201007_20201018_02_T1_B2.TIF')
image2 = io.imread('C:/Users/asus/Downloads/LC08_L1TP_178034_20201007_20201018_02_T1_B3.TIF')
image3 = io.imread('C:/Users/asus/Downloads/LC08_L1TP_178034_20201007_20201018_02_T1_B4.TIF')
image4 = io.imread('C:/Users/asus/Downloads/LC08_L1TP_178034_20201007_20201018_02_T1_B5.TIF')


# In[101]:


B1 = np.array(image1).astype(float)
B2 = np.array(image2).astype(float)
B3 = np.array(image3).astype(float)
B4 = np.array(image4).astype(float)


# In[102]:


blue = (B1-np.min(B1))/(np.max(B1)-np.min(B1))
green = (B2-np.min(B2))/(np.max(B2)-np.min(B2))
red = (B3-np.min(B3))/(np.max(B3)-np.min(B3))
nir = (B4-np.min(B4))/(np.max(B4)-np.min(B4))


# # NDVI Calculation for 2020 Image

# In[103]:


#NDVI
NDVI2 = (nir-red)/(nir+red)


# In[104]:


plt.figure(figsize=(15,10))
plt.imshow(NDVI2, cmap=cm.Greys)
plt.title('NDVI Image')
plt.colorbar()
plt.axis('off')
plt.show()


# In[105]:


NDV2 = io.imsave(fname="NDVI20.tif", arr=NDVI2)


# In[106]:


rgb = np.stack([nir, red, green], axis=2)
threshold = 0.2
veg = NDVI2 > threshold
non_veg = NDVI2 <= threshold


# In[107]:


fig , ax = plt.subplots(nrows=2, ncols=2, figsize=(15,15))
ax[0,0].imshow(rgb)
ax[0,0].set_title('RGB Image')
ax[0,0].axis('off')
######
ax[0,1].imshow(NDVI2, cmap=cm.Greens)
ax[0,1].set_title('NDVI-Image')
ax[0,1].axis('off')
######
ax[1,0].imshow(veg, cmap=cm.Greens)
ax[1,0].set_title('Vegetation-Area')
ax[1,0].axis('off')
######
ax[1,1].imshow(non_veg, cmap=cm.Blues)
ax[1,1].set_title('Non-Vegetation Area')
ax[1,1].axis('off')
plt.show()


# # NDWI Calculation for 2020 Image

# In[108]:


#NDWI
NDWI20 = (green - nir)/(green + nir)


# In[109]:


plt.figure(figsize=(15,10))
plt.imshow(NDWI20, cmap=cm.gray)
plt.title('NDWI20 Image')
plt.colorbar()
plt.axis('off')
plt.show()


# In[110]:


NDWI2 = io.imsave(fname="NDWI20.tif", arr=NDWI20)


# In[119]:


rgb = np.stack([nir, red, green], axis=2)
threshold = 0.07
water2 = NDWI20 > threshold
non_wat2 = NDWI20 <= threshold


# In[120]:


fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(15,15))

######
ax[0].imshow(water2, cmap=cm.Greens)
ax[0].set_title('Water-Area')
ax[0].axis('off')
######
ax[1].imshow(non_wat2, cmap=cm.Reds)
ax[1].set_title('Non-Water Area')
ax[1].axis('off')
plt.show()

