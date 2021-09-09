import sys

inputs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '':
        break
    inputs.append(line)

while len(inputs) > 0:
    link_nums = int(inputs.pop(0))
    class ListNode:
        def __init__(self, val):
            self.m_nKey = val
            self.m_pNext = None

    root = []
    ans = 0
    nodes = inputs.pop(0).split(' ')
    nodes = list(filter(lambda x: x != '', nodes))
    get_i = link_nums - int(inputs.pop(0))
    for i in range(len(nodes)):
        if i == get_i:
            ans = int(nodes[i])

    print(ans)