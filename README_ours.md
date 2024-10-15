# Installation Process

- First install all required things from the original Ground-SAM2
- Download the checkpoint using `./checkpoints/download_ckpts.sh` (we only use sam2.1_hiera_large.pt).


### Runnable Script
```
1. Convert the png images into jpeg (only support jpeg or jpg format)
python3 -m convert_png_to_jpg --input_dir [path to png dir] --output_dir [path to jpg dir]
python3 -m grounded_sam2_tracking_demo --input_dir [path to jpg dir] --output_dir [path to store masks and segmentation results] --text [text prompt for segmentation]

```