def trans(n):
    if len(n) == 0:
        return [[]]
    res_n = []
    for el in trans(n[:-1]):
        for i in range(len(el) + 1):
            el_new = el[:]
            el_new.insert(i, n[-1:][0])
            res_n.append(el_new)
    return res_n


res = trans(list(range(1, int(input()) + 1)))
for elw in res:
    print(*elw)

