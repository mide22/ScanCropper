import argparse, os
from settings import Settings

class ArgParser:

	@staticmethod
	def parse():
		parser = argparse.ArgumentParser(description="Scanned image cropper." +
			"\nProcess scanned images to find photos inside them." +
			"\nOrients and crops photos found in the image scan." +
			"\nProcesses all images found in the input directory, and" +
			"\nwrites all found and processed photos in the output directory." +
			"\nCan process multiple photos in a single scan.",
			formatter_class=argparse.ArgumentDefaultsHelpFormatter)
		parser.add_argument('--dir', '-d', type=str, default=os.environ.get('SC_DIR'),
							help="Specify the location of the scans to process.")
							
		parser.add_argument('--odir', '-o', type=str, default=os.environ.get('SC_ODIR'),
							help="Specify where to save the output images.")

		parser.add_argument('--pdir', '-po', type=str, default=os.environ.get('SC_ODIR_PROCESSED'),
							help="Specify where to move the processed input scans. If option is empty files will not moved.")

		parser.add_argument('--watch', '-w', action=argparse.BooleanOptionalAction, default=os.environ.get('SC_WATCH', False),
							help="Specify weather to watch input location for new scans and process them.")

		parser.add_argument('--polling-timeout', type=int, dest='polling_timeout', default=os.environ.get('SC_POLLING_TIMEOUT', 0),
							help="With --watch the --polling-timeout set the timeout in seconds of the observer. If 0 (default), typical observer is used - but it does not work on network shares. So set a time out > 0 for using PollingObserver.")

		parser.add_argument('--no-dirscan', dest='no_dirscan', action=argparse.BooleanOptionalAction, default=os.environ.get('SC_NO_DIRSCAN', False),
							help="Specify weather to NOT scan input location on start and process all supported files.")
		
		parser.add_argument('--output-format', '-of', type=str, default=os.environ.get('SC_OUTPUT_FORMAT', 'jpg'),
							help='Defines the image output format (jpg or png).')

		parser.add_argument('--output-jpeg-quality', type=int, dest='output_jpeg_quality', default=os.environ.get('SC_OUTPUT_JPEG_QUALITY', 85),
							help="Quality of jpeg results. Range [1,100]")

		parser.add_argument('--manual-name', '-mn', action='store_true',
							help='Manually name each photo.')

		parser.add_argument('--manual-metadata', '-mm', action='store_true',
							help='Manually add metadata to each photo. Only works if --output-format jpg')

		parser.add_argument('--thresh', '-t', type=int, dest='thresh', default=os.environ.get('SC_THRESH', 230),
							help="Sets the threshold value when determining photo edges." +
							"\nUse higher values for brighter images. Lower for tighter cropping." +
							"\nRange [0,255]")

		parser.add_argument('--blur', '-b', type=int, dest='blur', default=os.environ.get('SC_BLUR', 9),
							help="How much blur to apply when processing." +
							"\nDifferent values may effect how well scans are found and cropped." +
							"\nMust be odd number greater than 1.")

		parser.add_argument('--output-file-name-prefix', '-p', dest='output_file_name_prefix', type=str, default=os.environ.get('SC_OUTPUT_FILE_NAME_PREFIX', ''),
							help="Append the prefix string to the start of output image file names.")

		parser.add_argument('--output-file-name-prefix-strftime', dest='output_file_name_prefix_strftime', type=str, default=os.environ.get('SC_OUTPUT_FILE_NAME_PREFIX_STRFTIME', ''),
							help="Append the strftime-formatted prefix string to the start of output image file names.")
		args = parser.parse_args()

		
		# Check if input and output directories are specified.
		if args.dir is None or args.odir is None:
			raise Exception("Input and Output directory must be specified")

		return Settings(args.thresh, args.blur, args.dir, args.odir, args.pdir, args.watch, args.polling_timeout, args.no_dirscan, args.output_file_name_prefix, args.output_file_name_prefix_strftime, args.manual_name, args.manual_metadata, args.output_format, args.output_jpeg_quality)
