from enum import Enum

class ErrCodes(Enum):
	e_00 = "FilesysErr|DIR_NON_EXIST"
	e_01 = "FilesysErr|BUNDLE_DIR_NON_EXIST"
	e_10 = "AudioErr|INVALID_FORMAT"
	e_99 = "ErrOther|UNKNOWN_ERR"