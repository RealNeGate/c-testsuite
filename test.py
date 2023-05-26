import glob
import subprocess

good = 0
total = 0

list = glob.glob("tests/single-exec/*.c")

print("[Click for summary](#summary)\n\n")

print("## Raw results\n")

for f in list:
	total += 1
	result = subprocess.run(["sh", "./runners/single-exec/cuik-x86_64", f], capture_output=True)

	print(f"# Test `{f}`\n")
	print("```\n")
	print(result.stdout.decode('utf-8'))
	print(result.stderr.decode('utf-8'))
	print("```\n")

	if result.returncode == 0:
		good += 1

print("## Summary\n")
print(f"passed {good} out of {total}")
