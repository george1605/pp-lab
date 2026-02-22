import sys

with open(sys.argv[1], "r+") as f:  # python3 main.py <file>
	content = f.read()
	sep = ".,;:!?\'\""
	for s in sep:
		content = content.replace(s, "")
	print("Content: ", content)
	f.seek(0)
	f.write(content)
	f.truncate() 
