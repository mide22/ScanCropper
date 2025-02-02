# ScanCropper

ScanCropper is a Python script designed to identify, crop, and correctly orient photographs in scanned images (".jpg", ".jpeg", ".png", ".pdf", ".bmp"). It is particularly suited for finding rectangular images on a white background. It can handle multiple photos in a single scan and process multiple scanned images at once, meaning you don't have to perfectly align the photos in your scanner. Furthermore, there is the option to manually name and add metadata to each extracted image (an image preview is given).

PDF scans are converted into a png with a default dpi of 600 (can be changed in `scan_cropper.py`) before extracting the images.
Make sure that the pdf scans only have a length of one page.
## Use Case Example

Suppose you have a photo album and you scan 3 photos at a time, leaving some space between them on the scanner. For each file it processes, it will output 3 individual, cropped, and correctly oriented photos from the scan.

```bash
python3 scan_cropper.py --photos-per-scan 3 --dir ./scans --odir ./images --manual-name --manual-metadata
```

<p>Example Scan:</p>
<img src="./scans/input/example-3.png" width="500" alt="Scanned input file in .png format">

<p>Result Image 0:</p>
<img src="./scans/results/example-3_00.jpg" width="300" alt="Output image 0">

<p>Result Image 1:</p>
<img src="./scans/results/example-3_01.jpg" width="300" alt="Output image 1">

<p>Result Image 2:</p>
<img src="./scans/results/example-3_02.jpg" width="450" alt="Output image 1">

## Requirements

- Python 3.9 or above
- OpenCV
- NumPy
- PyMuPDF
- pillow
- py3exiv2

You can install the required Python packages with pip:

```bash
pip install opencv-python-headless numpy PyMuPDF pillow
```

In order to manually add metadata to each image metadata to the files when using `--manual-metadata` you also need:

```bash
pip install py3exiv2
```

If you get an error when installing this package it is likely that certain dependencies are missing. On Ubuntu install them with:
```bash
sudo apt-get install build-essential python-all-dev libexiv2-dev libboost-python-dev
```

## Usage

Navigate to the directory containing the ScanCropper script:

```bash
cd /path/to/ScanCropper
```

Run the script, specifying the input directory (containing your scanned images) and the output directory (where the cropped images will be saved):

```bash
python scan_cropper.py --dir /path/to/input/dir --odir /path/to/output/dir
```

You can customize the processing with several options. Here are some, have a look to [arg_parse.py](arg_parse.py) for more and using environment variables:

    `--dir`                     or  `-d`    Specify the location of the scans to process.
    `--odir`                    or  `-o`    Specify where to save the output images.
    `--pdir`                    or  `-po`   Specify where to move processed scans.
    `--output-format`           or  `-of`   Defines the image output format [jpg (default) or png].
    `--output-jpeg-quality`                 Defines the quality of jpeg image output, 1-100.
    `--watch`                   or  `-w`    Specify weather to watch input location for new scans and process them.
    `--manual-name`             or  `-mn`   Independently shows each image and asks for the image name before saving.
    `--manual-metadata`         or  `-mm`   Independently shows each image and asks for individual metadata to attach to the image (only possible for jpg as output format).
    `--num-threads`             or  `-n`    Number of threads to use (default: system number of cores).
    `--thresh`                  or  `-t`    Threshold value for determining photo edges. Use higher values for brighter images, lower for tighter cropping (default: 230).
    `--blur`                    or  `-b`    Amount of blur to apply when processing. Different values may affect how well scans are found and cropped. Must be an odd number greater than 1 (default: 9).
    `--output-file-name-prefix` or  `-p`    Prefix string to append to the start of output image file names.
    `--output-file-name-prefix-strftime`    Prefix string, strftime formatted to get datetime.


## Credit
This project is an up to date and extended version of https://github.com/murniox/ScanCropper, 
which is an up to date and extended version of https://github.com/kosenina/ScannedImageMultiCrop/tree/master.

Usefull links:

    https://github.com/polm/ndl-crop
    https://flothesof.github.io/removing-background-scikit-image.html
    https://github.com/Claytorpedo/scan-cropper/


