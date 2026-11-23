import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def bin_img(image : np.ndarray, bin_size : int = 10): 

    height,width = np.shape(image)

    new_height = (height //bin_size)*bin_size

    new_width = (width // bin_size)*bin_size

    truncated_img = image[:new_height, :new_width]

    super_pixels = truncated_img.reshape(height // bin_size, bin_size, width // bin_size, bin_size).swapaxes(1,2)

    super_pixel_arr = np.mean(super_pixels, axis = (2,3))

    return super_pixel_arr

def plot_comparison(original_img : np.ndarray, down_sampled_img : np.ndarray, bin_size : int = 10,):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # 2. Plot the original image on the left
    axes[0].imshow(original_img, cmap='gray')
    axes[0].set_title(f"Original Image\n({original_img.shape[1]}x{original_img.shape[0]})")
    axes[0].axis('off')  # Hide grid lines and pixel ticks

    # 3. Plot the superpixel (downsampled) image on the right
    # Note: 'interpolation="nearest"' prevents matplotlib from blurring the blocks
    axes[1].imshow(down_sampled_img, cmap='gray')
    axes[1].axis('off')

    # Display the plot
    plt.tight_layout()
    plt.show()


#rows are shifted then columns 

def shift_pixels(shift: float, og_img : np.ndarray, bin_size : int = 10):

    real_shift = shift * 10

    shifted_rows = np.roll(og_img, real_shift, axis = 1)

    shifted_img = np.roll(shifted_rows, shift, axis = 0)

    binned_shifted = bin_img(shifted_img, bin_size)


    return binned_shifted 

