import os 
from error_handler.report_err import report_err
class AutoMixer:
	#todo extract this to config?
	valid_audio_formats = ['m4a', 'mp3']
	def validate_active_dir(self, input_dir):
		active_dir_exists = os.path.exists(self.active_dir)
		#check if active dir exists
		if active_dir_exists:
			self.active_dir = input_dir
		else:
			#first on-the-spot test of error reporting
			print(report_err("e_00", self.active_dir))
			
	def __init__(self, input_dir):
		#TODO: validate input dir before assigning
		#TODO: instantiate IO and Error handler
		#TODO: parse (optional) user config for settings and smix-ins
		#TODO: never considered, bu use and instantiate separate track manager?
		"""
			- validate input dir and set as active dir
			- load config and parse settings
			- verify audio in sub-folder of active dir (correct extensions)
			- create new working directory (temp) and clean filenames by copy + rename in numerical order
			- verify mix-ins and copy / rename, add to working directory -> different name scheme from main audios
			- use track handler to import + memoize (manage info in memory for quick retieval/macro selection)
			- macro factory functions?

		"""
		self.validate_active_dir(os.path.abspath(input_dir))