from err_codes import ErrCodes
from err_codes_map import *

class ErrHandler:

	def __init__(self):

	#type = enum class for error type
	#code = member of enum class
	#blame = for msg formatting, where did error come from? (could be filename or filepath etc)
	def report_err(code, blame):
		 err_type, specific_err = err_codes[code].split("|")
		 if err_type in err_codes_map:
		 	if specific_err in err_codes_map[err_type]:
		 		#TODO restructure blame as a list
		 		err_msg = err_codes_map[err_type][specific_err].format(blame)
		 		 return err_msg
		 	else:




