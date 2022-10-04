import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# get required images
if not os.path.isdir('Images'):
  !wget -O watermarking-images.zip "https://drive.google.com/uc?export=download&id=1GOz-jcICYEFZwMgzZdNEP3j7ZMDXIOuo"
  !unzip watermarking-images.zip



# Read image and mark
im = cv2.imread('Images/lena.bmp', 0)
print('Image shape: ', im.shape)

wat = cv2.imread('Images/mark.png', 0)
print('Watermark shape: ', wat.shape)


# Flatted the images for easy embedding: it's easier this way
# The watermark must have a dimension equal (or smaller) than the one of the image
res_flat = im.flatten()
wat_flat = wat.flatten()

N = res_flat.shape[0]

# Example of decoded pixel value
pixel = format(res_flat[0], "08b")
print(pixel)
print(type(pixel))

# Embedding
for i in range(N):
  im_pixel_to_binary = format(res_flat[i], "08b")
  wat_pixel_to_binary = format(wat_flat[i], "08b")
  
  # concate all the pixels until the LSB from the image
  # and the MSB of the watermark as LSB
  res_pixel = im_pixel_to_binary[:7] + wat_pixel_to_binary[0]

  res_flat[i] = int(res_pixel, 2)



# Reshape image
res = res_flat.reshape(512, 512)

# Show images side by side
plt.subplot(121)
plt.title('Original')
plt.imshow(im, cmap='gray')
plt.subplot(122)
plt.title('Watermarked')
plt.imshow(res,cmap='gray')
plt.show()

# save image
#res = Image.fromarray(res)
#res.save('watermarked.bmp')
cv2.imwrite('watermarked.bmp', res)