from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import numerical_binning

images = []

for i in range(10):
    filename = f'Repeats_10/Image_{i:04d}_0.tiff'
    img = Image.open(filename).convert('L')
    images.append(np.array((img), dtype = np.float32))

images_stack = np.stack(images,axis = 0)

average_img = np.asarray(np.mean(images_stack,axis = 0))

#binned = numerical_binning.bin_img(average_img, bin_size = 10)


#numerical_binning.plot_comparison(average_img, binned)

#shifted, shifted_binned = numerical_binning.shift_pixels(shift = 0.1, og_img = average_img)

#print(np.shape(shifted_binned))
numerical_binning.rigid_body_motion(average_img, shift = 0.1, save_path = Path("results/real-images") )
