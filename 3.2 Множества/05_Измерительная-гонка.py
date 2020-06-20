n = int(input())
dict_ = {}
for i in range(n):
    res = 0.0
    set1 = set(list(map(int, input().split())))
    set2 = set(list(map(int, input().split())))
    set3 = set1.intersection(set2)
    for el in set3:
        res += el
    res /= len(set1)
    dict_[i + 1] = res
max_ = 0.0
for el in dict_:
    if dict_.get(el) > max_:
        max_ = dict_.get(el)
e = 0
for el in dict_:
    e += 1
    if dict_.get(el) == max_:
        print(e)



# dict1 = {
#     1: res
#     2:
#
# }

# n = int(input())
# dict_ = {}
# for i in range(n):
#     res = 0.0
#     frst_l = list(map(int, input().split()))
#     scnd_l = list(map(int, input().split()))
#     for j in range(len(frst_l)):
#         res += abs(scnd_l[j] - frst_l[j])
#     res /= len(frst_l)
#     dict_[i + 1] = res
# print(dict_)