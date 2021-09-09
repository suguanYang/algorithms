import sys

inputs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '':
        break
    inputs.append(line)

while len(inputs) > 0:
    [n, k] = inputs.pop(0).split(' ')
    arr = filter(lambda x: x.isdigit(), inputs.pop(0).split(' '))

    res = []

    sor = sorted(arr, key = lambda x: int(x))

    print(' '.join(sor[0:int(k)]))
