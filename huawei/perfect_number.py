import sys
inputs = []

for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '':
        break
    inputs.append(line)

res = []
dict = {}
while len(inputs) > 0:
    num = int(inputs.pop(0))
    acc = 0
    while num > 0:
        if dict.get(num):
            acc+=1
        else:
            max_factor = num // 2

            factors = []
            for i in range(1, max_factor + 1):
                if num % i == 0:
                    factors.append(i)

            if sum(factors) == num:
                acc += 1
                dict[num] = True
        num -= 1

    res.append(acc)

for i in res:
    print(i)