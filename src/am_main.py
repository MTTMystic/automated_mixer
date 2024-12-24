import os 

class AutoMixer:
	def validate_input():
		active_dir_exists = os.path.exists(active_dir)
		#check if active dir exists
		if active_dir_exists:
			pass
		else:
			print()

	def __init__(self, input_dir):
		#TODO: validate input dir before assigning
		#TODO: instantiate IO and Error handler
		#TODO: parse (optional) user config for settings and mix-ins
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
		self.active_dir = self.path.abspath(input_dir)
		