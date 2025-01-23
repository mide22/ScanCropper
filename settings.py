import math as m

class Settings:
	def __init__(self, threads, thresh, blur, scale, input_dir, output_dir, processed_dir, watch, polling_timeout, no_dirscan, output_file_name_prefix, output_file_name_prefix_strftime, manual_name, manual_metadata, output_format, output_jpeg_quality):
		self.threads = threads
		self.thresh = thresh
		self.blur = blur
		self.scale = scale
		self.input_dir = input_dir
		self.output_dir = output_dir
		self.processed_dir = processed_dir
		self.watch = watch
		self.polling_timeout = polling_timeout
		self.no_dirscan = no_dirscan
		self.output_file_name_prefix = output_file_name_prefix
		self.output_file_name_prefix_strftime = output_file_name_prefix_strftime
		self.manual_name = manual_name
		self.manual_metadata = manual_metadata
		self.output_format = output_format
		self.output_jpeg_quality = output_jpeg_quality
		self.image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]
		self.supported_file_patterns = ["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.pdf"]
		self.deg_to_rad = m.pi / 180
		self.max = 255  # Thresholded max value (white).
		self.retries_loading_file = 10  # Number of times to retry loading a file before giving up

	def __str__(self):
		return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
