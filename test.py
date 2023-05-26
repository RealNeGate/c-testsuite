import glob
import subprocess

good = 0
total = 0

list = glob.glob("tests/single-exec/*.c")

for f in list:
	total += 1
	result = subprocess.run(["sh", "./runners/single-exec/cuik-x86_64", f])
	if result.returncode == 0:
		good += 1

print(f"Summary:\n  passed {good} out of {total}")
