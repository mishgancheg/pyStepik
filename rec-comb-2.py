def rec_comb(n):
    if len(n) == 0:
        return [[]]
    if len(n) == 1:
        return [[], [n[0]]]
    arrm1 = rec_comb(n[:-1])
    return arrm1 + list(map(lambda a: a + n[-1:], arrm1))


res1 = list(map(sorted, rec_comb(list(map(int, input().split(' '))))))
res1.sort(key=len)
print(*list(map(lambda el: '{' + ', '.join(map(str, el)) + '}', res1)))
