def rec_comb(n):
    arr_in_arr = [[]]
    for el in n:
        arr_in_arr += [s + [el] for s in arr_in_arr]
    return arr_in_arr


arrOfNums = [1, 2, 3, 4]  # list(map(int, input().split(' ')))
print(arrOfNums)
newArr = rec_comb(arrOfNums)
print(newArr)
for arr in newArr:
    if len(arr) > 0:
        n_a = str(arr).replace('[', '').replace(']', '')
        print('{', *n_a.split(' '), '}')
    else:
        print("{}")
