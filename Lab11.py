import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. IMAGE PROPERTIES (HEIGHT, WIDTH, SHAPE, MIN BLUE VALUE)
img = Image.open(r"C:\Users\DELL\Downloads\MU.jpg")
img_array = np.array(img)
height = img_array.shape[0]
width = img_array.shape[1]
shape = img_array.shape
min_blue = np.min(img_array[:, :, 2])
print("===== PROGRAM 1: IMAGE PROPERTIES =====")
print("Image Dimensions (Height x Width):", (height, width))
print("Shape of the Image (H x W x Channels):", shape)
print("Minimum Pixel Value at Blue Channel:", min_blue)
print()

# 2. PAD THE IMAGE AND DISPLAY BOTH ORIGINAL + PADDED
pad_top, pad_bottom = 50, 50
pad_left, pad_right = 50, 50
padded_img = np.pad(
    img_array,
    ((pad_top, pad_bottom), (pad_left, pad_right), (0, 0)),
    mode='constant',
    constant_values=0
)
print("===== PROGRAM 2: IMAGE PADDING DONE =====")
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(padded_img)
plt.title("Padded Image (Black Borders)")
plt.axis("off")
plt.tight_layout()
plt.show()

# 3. RGB CHANNEL EXTRACTION AND DISPLAY
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]
print("===== PROGRAM 3: RGB CHANNEL EXTRACTION =====")
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(R, cmap='Reds')
plt.title("Red Channel")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(G, cmap='Greens')
plt.title("Green Channel")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(B, cmap='Blues')
plt.title("Blue Channel")
plt.axis("off")
plt.tight_layout()
plt.show()
