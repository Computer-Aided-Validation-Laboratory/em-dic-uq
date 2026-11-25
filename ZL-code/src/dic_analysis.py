from pathlib import Path
from pyvale import  dic
import matplotlib.pyplot as plt
import numpy as np

ref_img = Path("results/real-images/ref_image.tiff")
def_img = Path("results/real-images/deformed_image_*.tiff")

output_path = Path("results/pyvale-output")
output_path.mkdir(parents=True, exist_ok=True)

roi = dic.RegionOfInterest(ref_img)
# roi.interactive_selection()
roi.rect_boundary(0,0,0,0)
#roi_file = output_path / "roi.dat"
#roi.save_array(filename=roi_file, binary=False)

#roi.read_array(filename=roi_file, binary=False)

"""
dic.calculate_2d(reference=ref_img,
                 deformed=def_img,
                 roi_mask=roi.mask,
                #  seed=roi.seed,
                 seed=[20,20],
                 subset_size=31,
                 subset_step=10,
                 shape_function="AFFINE",
                 max_displacement=10,
                 threshold=0.8,
                 correlation_criteria="ZNSSD",
                 output_basepath=output_path,
                 output_delimiter=",",
                 output_prefix="dic_results_",
                 print_level=1)
"""

dic_files = output_path / "dic_results_deformed_image_*.csv"
dicdata = dic.import_2d(data=dic_files, delimiter=",", binary=False)

#print(dicdata.shape())

fig, axes = plt.subplots(3, 2, figsize=(10, 15))

im1 = axes[0,0].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.u_px[0])
im2 = axes[0,1].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.v_px[0])

axes[0,0].set_title('u component (0.1 pixel shift)')
axes[0,1].set_title('v component (0.1 pixel shift)')

im3 = axes[1,0].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.u_px[2])
im4 = axes[1,1].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.v_px[2])

axes[1,0].set_title('u component (1 pixel shift)')
axes[1,1].set_title('v component (1 pixel shift)')

im5 = axes[2,0].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.u_px[9])
im6 = axes[2,1].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.v_px[9])

axes[2,0].set_title('u component (0.9 pixel shift)')
axes[2,1].set_title('v component (0.9 pixel shift)')



fig.colorbar(im1, ax=axes[0,0])
fig.colorbar(im2, ax=axes[0,1])
fig.colorbar(im3, ax=axes[1,0])
fig.colorbar(im4, ax=axes[1,1])
fig.colorbar(im5, ax=axes[2,0])
fig.colorbar(im6, ax=axes[2,1])
#plt.tight_layout()
plt.show()