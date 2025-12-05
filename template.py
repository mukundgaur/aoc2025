with open("input.txt", 'r') as f:
	lines = f.readlines()
	for line in lines:
		chars = list(line)
		ints = [int(x) for x in chars]
