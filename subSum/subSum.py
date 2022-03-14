def sub_sum(seq, t):
    sub_seq = {}
    sub_seq[(0, 0)] = True

    seq_l = len(seq)

    if t == 0:
        return True
    
    for i in range(t):
        sub_seq[(seq_l - 1, i)] = False

    acc = t
    for i in range(seq_l - 2, -1, -1):
        sub_seq[(i, t)] = sub_seq.get((i + 1, acc - seq[i])) or sub_seq.get((i + 1, acc))


    return sub_seq.get(0, t)