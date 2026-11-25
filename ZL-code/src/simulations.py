"""Run image-processing simulations for speckle patterns."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import numerical_binning

img = Image.open('test-speckles/SPeckle_pattern_test.bmp').convert('L')

img_arr = np.array(img)

binned = numerical_binning.bin_img(img_arr, bin_size = 10)
numerical_binning.plot_comparison(img_arr, binned)


numerical_binning.rigid_body_motion(img_arr,shift = 0.1, save_path = Path("results/simulations") )

