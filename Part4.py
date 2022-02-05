import os
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import nibabel as nib

#Reference: "https://www.youtube.com/watch?v=Tc9ONZLBHP0&ab_channel=DataScienceGarage"

mri_file = 'T2.nii.gz'

img_obj = nib.load(mri_file)

print(type(img_obj))

print(img_obj.shape)

image_data = img_obj.get_fdata()

print(type(image_data))
print("Image Data shape",image_data.shape)
# Get the image shape and print it out
height, width, depth = image_data.shape

maxval = 255

i = np.random.randint(0,maxval)
print(i)

plt.imshow(image_data[165,:,:], cmap = 'gray')
#plt.legend()
plt.title('Image when input is sliced along height with gray colormap')
plt.axis('off')
plt.show()


