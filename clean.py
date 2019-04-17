
files = ['config.py','language_map.py','main.py','preprocess.py','_preprocess.py','clean.py']
dirs = ['languages','test_language']

import os
import shutil

f = os.listdir()

for d in f:
	if os.path.isfile(d):
		if d not in files:
			os.remove(d)
	elif d not in dirs:
		shutil.rmtree(d)