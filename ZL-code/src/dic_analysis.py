from pathlib import Path

from pyvale import  dic

ref_img = Path("results/simulations/ref_image.tiff")
def_img = Path("results/simulations/deformed_image_*.tiff")

output_path = Path("results/pyvale-output")
output_path.mkdir(parents=True, exist_ok=True)

roi = dic.RegionOfInterest(ref_img)
# roi.interactive_selection()
roi.rect_boundary(0,0,0,0)
#roi_file = output_path / "roi.dat"
#roi.save_array(filename=roi_file, binary=False)

#roi.read_array(filename=roi_file, binary=False)


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


dic_files = output_path / "dic_results_*.csv"
dicdata = dic.import_2d(data=dic_files, delimiter=",", binary=False)

#fig, axes = plt.subplot(1, 2, figsize=(12, 6))

#axes[0].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.u_px)
#axes[1].pcolor(dicdata.ss_x, dicdata.ss_y, dicdata.v_px)

#plt.tight_layout()
#plt.show()