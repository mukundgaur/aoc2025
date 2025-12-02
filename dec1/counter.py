with open('input.txt', 'r') as f:
    lines = f.readlines()
    start = 50
    counter = 0
    for line in lines:
        val = int(line[1 : ])
        if (line[0] == 'R'):
            counter += (start + val) // 100
            start = (start + val) % 100
        else:
            if (start > 0):
                counter += (val - start) // 100 + 1
            elif start == 0:
                counter += (val - start) // 100
            start = (start - val) % 100
    print(counter)
