import sys

inputs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '':
        break
    inputs.append(line)
res = []
while len(inputs) > 0:
    num = int(inputs.pop(0))
    if num < 7:
        res.append(0)
        continue
    
    acc = 0
    for i in range(7, num + 1):
        if i % 7 == 0:
            acc += 1
        elif '7' in str(i):
            acc += 1
    
    res.append(acc)

for i in res:
    print(i)