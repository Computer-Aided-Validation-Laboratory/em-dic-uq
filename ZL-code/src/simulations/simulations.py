import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

from generated_images import bin_img, plot_comparison, shift_pixels


img = Image.open('speckle_pattern.png').convert('L')
img.save('greyscale_speckles.png')

img_arr = np.array(img)

super_pixel_img = bin_img(img_arr, bin_size= 20)

plot_comparison(img_arr, super_pixel_img, 20)

shifted1 = shift_pixels(shift = 0.1, og_img= img_arr, bin_size= 20)

plot_comparison(super_pixel_img, shifted1)

