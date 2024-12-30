import os 
from err_handler.err_handler import ErrHandler
from validation_handler.validation_handler import ValidationHandler

class AutoMixer:
	#todo extract this to config?
	
	#this is the name the user has to use for the subfolder that contains the subs to be bundled
	#other subfolders are junk and ignored
	"""
	bundle_dir_name = "bundle_subs"
	def validate_active_dir(self, input_dir):
		input_dir_exists = os.path.exists(input_dir)
		#check if active dir exists
		if input_dir_exists:
			self.active_dir = input_dir
			bundle_subs_dir = os.path.join(self.active_dir, self.bundle_dir_name)
			bundle_dir_exists = os.path.exists(bundle_subs_dir)
			if not (bundle_dir_exists):
				print(report_err("e_01", bundle_subs_dir))
			else:
				self.bundle_subs_dir = bundle_subs_dir
		else:
			#first on-the-spot test of error reporting
			print(report_err("e_00", input_dir))
	def validate_audio_files(self):
		#TODO mixin feature will include searching for mixins and validating them as well
		audio_file_list = os.listdir(self.bundle_subs_dir)
		for audio_fn, idx in audio_file_list:
			fn_main, ext = os.path.splitext(audio_fn)
			if ext[1:] in valid_audio_formats:
				pass
			else:
				print(report_err("e_10", audio_fn))
	def __init__(self, input_dir):
		#TODO: validate input dir before assigning
		#TODO: instantiate IO and Error handler
		#TODO: parse (optional) user config for settings and smix-ins
		#TODO: never considered, bu use and instantiate separate track manager?
		
			- validate input dir and set as active dir
			- load config and parse settings
			- verify audio in sub-folder of active dir (correct extensions)
			- create new working directory (temp) and clean filenames by copy + rename in numerical order
			- verify mix-ins and copy / rename, add to working directory -> different name scheme from main audios
			- use track handler to import + memoize (manage info in memory for quick retieval/macro selection)
			- macro factory functions?
		self.validate_active_dir(os.path.abspath(input_dir))
		"""
	

	def __init__(self):
		self.err_handler = ErrHandler()
		self.validation_handler = ValidationHandler()

		dev_config = validation_handler.load_dev_config()