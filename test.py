import glob
import subprocess

good = 0
total = 0

list = glob.glob("tests/single-exec/*.c")

print("[Click for summary](#summary)")

print("## Raw results ")
print("```\n")

for f in list:
	total += 1
	result = subprocess.run(["sh", "./runners/single-exec/cuik-x86_64", f])
	if result.returncode == 0:
		good += 1

print("```\n")

print("## Summary ")
print(f"passed {good} out of {total}")
