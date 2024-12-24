#TODO test reporting of errors and collection of errors (such as invalid auio input) to continue processes and report as aggregate

"""
Defining basic functionality of error handler which is abstracted from the specific types of errors and ideally from how errors are triggered

- Enums : each class of error (for example, validation error for input audio) is defined with enum
- Enum members : for each class of error the enum members define a string to be formatted -> simple
- (Advanced) could enum members somehow store information on callback fn or how to process error in more advanced cases? check if this arises

test points:
- if error enum does not exist then fail
- if error type ?(enum member) does not exist then fail
- in each case above the error handler reports (dev mode) that the error has been reported incorrectly (invalid error code)
- succeed when error category, code, and outcome (i.e. formatted string) match predefined corrrect response

-- btw dev mode should be in config.ini and enabled by default, but that cnfig is hidden from rando/per-use and a gitignore candidate

- specific error types - integration testing after specific other featues implemented + tests defined
- start by blueprint of code from am init: validation errors with input dir
- give invalid input in every way possible and ensure error is reported


"""

#FOR NOW, define basic error class with one report_err function and one error category, trigger as test
