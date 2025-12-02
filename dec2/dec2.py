import math
def checkValid(num):
    for i in range(1, len(num) // 2 + 1):
        check = num[0 : i]
        if (len(num) % len(check) != 0):
            continue
        endpoint = i 
        checker = False
        while (endpoint < len(num)):
            if (num[endpoint : endpoint + i] != num[0 : i]):
                checker = True
                break
            endpoint += len(check)
        if (not checker):
            return True
    return False
with open('input.txt', 'r') as f:
    lines = f.readlines()
    ranges = lines[0].strip().split(",")
    invalid = []
    for element in ranges:
        nums = element.split("-")
        num1 = int(nums[0])
        num2 = int(nums[1])
        for i in range(num1, num2 + 1):
            length = int(math.log(i, 10)) + 1
            if (checkValid(str(i))):
                invalid.append(i)
    print(sum(invalid))