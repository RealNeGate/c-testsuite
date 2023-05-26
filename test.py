import glob
import subprocess
import re

# 7-bit C1 ANSI sequences
ansi_escape = re.compile(r'''
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
''', re.VERBOSE)

good = 0
total = 0

list = glob.glob("tests/single-exec/*.c")

strs = []

for f in list:
	total += 1
	result = subprocess.run(["sh", "./runners/single-exec/cuik-x86_64", f], capture_output=True, text=True)

	strs.append(f"# Test `{f}`\n")
	strs.append("```\n")
	strs.append(ansi_escape.sub('', result.stdout))
	strs.append(ansi_escape.sub('', result.stderr))
	strs.append("```\n")

	if result.returncode == 0:
		good += 1

print("## Summary\n")
print(f"passed {good} out of {total}\n\n")

print("## Raw results\n")
print("\n\n".join(strs))
