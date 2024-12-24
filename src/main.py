from am import *
import sys

if __name__ == "__main__":
	#in future use config.ini for now stick to cml
	if (len(sys.argv) < 2):
		print("Error: Must provide active directory path")
	else:
		input_dir = sys.argv[1]
		automixer = AutoMixer(input_dir)
