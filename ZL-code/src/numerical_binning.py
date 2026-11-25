from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def bin_img(image : np.ndarray, bin_size : int = 10): 

    height,width = np.shape(image)

    new_height = (height //bin_size)*bin_size

    new_width = (width // bin_size)*bin_size

    truncated_img = image[:new_height, :new_width]

    super_pixels = truncated_img.reshape(height // bin_size, bin_size, width // bin_size, bin_size).swapaxes(1,2)

    super_pixel_arr = np.mean(super_pixels, axis = (2,3))

    return super_pixel_arr

def plot_comparison(original_img : np.ndarray, final_img : np.ndarray, bin_size : int = 10,):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # 2. Plot the original image on the left
    axes[0].imshow(original_img, cmap='gray')
    axes[0].set_title(f"Original Image\n({original_img.shape[1]}x{original_img.shape[0]})")
    axes[0].axis('off')  # Hide grid lines and pixel ticks

    # 3. Plot the superpixel (downsampled) image on the right
    # Note: 'interpolation="nearest"' prevents matplotlib from blurring the blocks
    axes[1].imshow(final_img, cmap='gray')
    axes[1].set_title(f"Binned Image\n({final_img.shape[1]}x{final_img.shape[0]})")

    axes[1].axis('off')

    # Display the plot
    plt.tight_layout()
    plt.show()


#rows are shifted then columns 

def shift_pixels(shift: float, og_img : np.ndarray, bin_size : int = 10):

    real_shift = shift * 10

    shifted_rows = np.roll(og_img, real_shift, axis = 1)

    shifted_img = np.roll(shifted_rows, -1 *real_shift, axis = 0)

    binned_shifted = bin_img(shifted_img, bin_size)

    return shifted_img,binned_shifted 

def rigid_body_motion(og_img: np.ndarray, shift: float, save_path: Path, deformed_images_number: int = 10, bin_size: int = 10):

    ref_img = bin_img(og_img, bin_size)

    ref_img_array = np.asarray(ref_img).astype(np.uint8)

    save_path.mkdir(parents=True, exist_ok=True)

    print(save_path.resolve())

    Image.fromarray(ref_img_array, mode='L').save(save_path/"ref_image.tiff")

    for i in range(0, deformed_images_number):
        deformed, deformed_binned = shift_pixels(shift + (i/ 10), og_img, bin_size)

        Image.fromarray(deformed_binned.astype(np.uint8), mode='L').save(save_path/f"deformed_image_{i}.tiff")

        print(f"Deformed image {i} saved at {save_path/f'deformed_image_{i}.tiff'}")


