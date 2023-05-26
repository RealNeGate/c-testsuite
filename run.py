import glob
import os
import subprocess

good = 0
total = 0

for f in glob.glob("tests/single-exec/*.c"):
	total += 1
	print(f)

	if subprocess.call(['cuik', f, '-c']) == 0:
		good += 1

print(f"Summary:\n  passed {good} out of {total}")
