with open("input.txt", 'r') as f:
	lines = f.readlines()
	grid = []
	for line in lines:
		line = line.strip()
		chars = list(line)
		grid.append(chars)
	# print(grid)
	pos = []
	def remove():
		overall = 0
		for row in range(len(grid)):
			for column in range(len(grid[row])):
				if (grid[row][column] != "@"):
					continue
				counter = 0
				if (row - 1 >= 0 and column - 1 >= 0 and grid[row - 1][column - 1] == "@"):
					counter += 1
				if (row - 1>= 0 and column >= 0 and grid[row - 1][column] == "@"):
					counter += 1
				if (row -1 >= 0 and column + 1 < len(grid[row]) and grid[row - 1][column + 1] == "@"):
					counter += 1
				if (row >= 0 and column + 1 < len(grid[row]) and grid[row][column + 1] == "@"):
					counter += 1
				if (row >= 0 and column - 1 >= 0 and grid[row][column - 1] == "@"):
					counter += 1
				if (row + 1 < len(grid) and column - 1 >= 0 and grid[row + 1][column - 1] == "@"):
					counter += 1
				if (row + 1 < len(grid) and column >= 0 and grid[row + 1][column] == "@"):
					counter += 1
				if (row + 1 < len(grid) and column + 1 < len(grid[row]) and grid[row + 1][column + 1] == "@"):
					counter += 1
				if (counter < 4):
					pos.append((row, column))
					overall += 1
		return overall
	tot = 0
	while True:
		pos = []
		cur = remove()
		if (cur == 0):
			break
		tot += cur
		for elem in pos:
			grid[elem[0]][elem[1]] = "."
	print(tot)
