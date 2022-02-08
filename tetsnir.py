#%%
import matplotlib.pyplot as plt
import pydicom

ds = pydicom.dcmread("./dicoms/n2d_0004.dcm")
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# print(ds)
# %%
