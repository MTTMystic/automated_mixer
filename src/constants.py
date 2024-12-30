from configparser import ConfigParser

class ConfigHandler:
	self._dev_config = ConfigParser()
	self._user_config = ConfigParser()
	def _load_dev_config(dev_config_fp):
		
