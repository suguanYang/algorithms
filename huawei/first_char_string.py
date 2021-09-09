import sys

inputs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '':
        break
    inputs.append(line)

length = int(inputs[0])

data = []
for i in range(1, length + 1):
    [seq, num, date] = inputs[i].split(' ')
    data.append({
        'seq': seq,
        'num': int(num),
        'date': date,
        'date_num': int(date.replace(':', ''))
    })

def quick_sort(ls, key):
    def parition(l, h):
        pivotValue = ls[h][key]
        pivotIndex = l

        for i in range(l, h):
            if ls[i][key] < pivotValue:
                [ls[i], ls[pivotIndex]] = [ls[pivotIndex], ls[i]]
                pivotIndex += 1

        [ls[pivotIndex], ls[h]] = [ls[h], ls[pivotIndex]] 
        return pivotIndex
    def quickSort(l, h):
        if l >= h:
            return

        p = parition(l, h)
        quickSort(l, p - 1)
        quickSort(p + 1, h)

    quickSort(0, length - 1);
    return ls;

res =quick_sort(data.copy(), 'num')
for d in res:
    print(str(d.get('num')) + ' ' + d.get('date') + ' ' + d.get('seq'))

res2 =quick_sort(data.copy(), 'date_num')
for d in res2:
    print(d.get('date') + ' ' + str(d.get('num')) + ' ' + d.get('seq'))
