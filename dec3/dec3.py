with open('input.txt', 'r') as f:
    lines = f.readlines()
    elems = []
    for line in lines:
        chars = list(line.strip())
        ints = [int(x) for x in chars]
        # print(ints)
        curmax = []
        curVal = 0
        for i in ints:
            if (len(curmax) < 12):
                curmax.append(i)
            else:
                strs = [str(x) for x in curmax]
                remember = -1
                for k in range(1, len(curmax)):
                    if (curmax[k] > curmax[k - 1]):
                        remember = k
                        break
                if (remember != -1):
                    l = curmax[0 : k - 1]
                    l.extend(curmax[k :])
                    curmax = l
                    curmax.append(i)
                if (remember == -1):
                    if i > curmax[11]:
                        curmax[11] = i   
        strs = [str(x) for x in curmax]  
        elems.append(int("".join(strs)))
    print(sum(elems))