import sys

inputs = []
for line in sys.stdin:
    a = line.replace('\n', '')
    if a == '':
         break
    inputs.append(a)

case = []

case_idx = 0
while len(inputs) > 0:
    case.append([])
    cache = dict()
    case_len = int(inputs.pop(0))
    for i in range(case_len):
        cur = int(inputs.pop(0))
        if cache.get(cur) == None:
            case[case_idx].append(cur)
            cache[cur] = cur
    case_idx+=1

def sort(list):
    prvot = list[0]

    def partion(arr, l, h):
        pivot = arr[h]
        p_idx = l
        for i in range(l, h):
            if arr[i] < pivot:
                arr[i], arr[p_idx] = arr[p_idx], arr[i]
                p_idx += 1
        arr[p_idx], arr[h] = arr[h], arr[p_idx]
        return p_idx
    
    def iter(arr, l, h):
        if l > h:
            return
        
        p = partion(arr, l, h)
        iter(arr, l, p - 1)
        iter(arr, p + 1, h)
    iter(list, 0, len(list) - 1)
    return list

for i in range(len(case)):
    sort(case[i])

for i in range(len(case)):
    for j in range(len(case[i])):
        print(case[i][j])