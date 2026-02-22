import sys

with open(sys.argv[1], "r+") as f:  # python3 main.py <file>
	content = f.read()
	sep = ".,;:!?\'\""
	for s in sep:
		content = content.replace(s, "")
	content = " ".join(s.split()) # split and join with 1 space (remove multiple spaces)
	print("Content: ", content)
	f.seek(0)
	f.write(content)
	f.truncate()
