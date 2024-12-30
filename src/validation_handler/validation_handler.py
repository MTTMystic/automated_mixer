
import os 
from configparser import ConfigParser

class ValidationHandler:

	def _load_dev_config(dev_config_fp)
		pass
	
	def __init__(self):
		"""
		#check that the dev config path exists
		abspath_dev_config = os.path.abspath(dev_config_filepath)
		dev_config_exists = os.path.exists(abspath_dev_config)
		if not dev_config_exists:
			#TODO replace with report_err(file_exists)
			print("dev config file not found at specified path")
		else:
			_load_dev_config(abspath_dev_config)
			"""
		pass

	class ConfigHandler:
		self._dev_config = ConfigParser()
		self._user_config = ConfigParser()
		def _load_dev_config(dev_config_fp):
