import PIL
from PIL import Image

images = []

for n in range(384):
    frame = Image.open("./img_seq/{}.png".format(n))
    images.append(frame)

# Save the frames as an animated GIF
images[0].save('brainmri.gif',
               save_all=True,
               append_images=images[1:],
               duration=50,
               loop=0)