from .err_codes import ErrCodes
from .err_codes_map import *

   
"""
for now let's see what happens if err handler is not a class - will I need class members later?
class ErrHandler:

	def __init__(self):
		pass 
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
		 		print(f"{spec_err} is not a valid error in class {err_type}".format(specific_err, err_type))
		 else:
		 	print(f"{err_type} is not a valid class of error".format(err_type))

 """


def report_err(code, blame):
	 err_type, specific_err = ErrCodes[code].value.split("|")
	 if err_type in err_codes_map:
	 	if specific_err in err_codes_map[err_type]:
	 		#TODO restructure blame as a list
	 		err_msg = err_codes_map[err_type][specific_err].format(blame)
	 		return err_msg
	 	else:
	 		print(f"{spec_err} is not a valid error in class {err_type}".format(specific_err, err_type))
	 else:
	 	print(f"{err_type} is not a valid class of error".format(err_type))
