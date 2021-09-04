import sys

inputs = []
for line in sys.stdin:
    a = line.replace('\n', '').replace('0x', '')
    if a == '':
         break
    inputs.append(a)

res = []

mapping = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

for i in range(0, len(inputs)):
    acc = 0
    for j in range(len(inputs[i])):
        weight = len(inputs[i]) - 1 - j
        acc += mapping.get(inputs[i][j].lower()) * 16 ** weight
    res.append(acc)

for i in range(len(res)):
    print(res[i])