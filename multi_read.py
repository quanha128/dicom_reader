#%%
import matplotlib.pyplot as plt
import pydicom
import glob

pixel_data = []
paths = glob.glob("./dicoms/*.dcm")
# fig, ax = plt.subplots(384 ,1, figsize=(800,800))
i=0
for path in paths:
    dataset = pydicom.dcmread(path)
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.savefig("{}.png".format(i))
    pixel_data.append(dataset.pixel_array)
    # img = dataset.pixel_array
    i+=1

# print(pixel_data)
# %%
