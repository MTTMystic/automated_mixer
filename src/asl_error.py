from enum import Enum

class FILESYS_ERROR(Enum):
    DIR_DOES_NOT_EXIST = "The input folder {0} does not exist."


    """
    Reports errors to user.
    err_type = enum class and member of error to report, for example FILESYS_ERROR.DIR_DOES_NOT_EXIST
    args = list of positional arguments for error string
    
    For example: report_error(FILESYS_ERROR, DIR_DOES_NOT_EXIST, "non_existent_folder_path")
                 -> user sees "The folder non_existent_folder_path does not exist".
    """
def report_error(err_type, args):
    err_string = err_type.value.format(*args)
    return (err_string)