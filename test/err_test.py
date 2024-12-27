"""
TEST CASES

DEV MODE ONLY
- given an invalid code, the report_err function should return with an error

- given a valid abbreviated error code (see err_codes) but no corresponding error in map, report what was needed (what err code specified to search in map)

- given invalid args for formatting err msg, report what was missing (if not enough positional arguments

- given invalid args for formatting err msg, report what was ' wrong'?
	- example: Error msg says "The input file [input_file_name] is invalid" but the actual arg given is a list of files instead of one name
	- example: Error msg says "The input file [input file name] is invalid" but the actual arg given is a number string?
	- may require more rigorous validation of error handling to be testable? error msgs require validation

GENERAL CASES
	- given a valid error code and formatting args, and no dev errors, report to user a correct error message (what should be given code, map, and format args)
	- 
	(integration test?) check that an error is reported in every case that should trigger an error - these must be done after further implementation progresses

- 



"""