import sys

inputs = []
for line in sys.stdin:
    a = line.replace('\n', '').split(' ')
    if a[0] == '0':
         break
    inputs.append(a)

for i in range(len(inputs)):
    inputs[i] = int(inputs[i][0])

def solution():
    def iter(n, acc):
        if n == 2:
            newer = 1
            older = 0
        else:
            newer = n // 3
            older = n % 3

        if newer < 1:
            return acc
        
        return iter(newer + older, acc + newer)
    
    res = []

    for i in range(len(inputs)):
        res.append(iter(inputs[i], 0))
    
    return res

output = solution()
for i in range(len(output)):
    print(output[i])