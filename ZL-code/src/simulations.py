"""Run image-processing simulations for speckle patterns."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import numerical_binning

img = Image.open('test-speckles/speckle_pattern.png').convert('L')

img.save('test-speckles/greyscale_speckles.png')

img_arr = np.array(img)

numerical_binning.rigid_body_motion(img_arr,shift = 0.1, save_path = Path("results/simulations") )

