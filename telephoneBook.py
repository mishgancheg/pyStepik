# dict_ = {}
# str_ = input()
# while str_ != '.':
#     arr = str_.split(' ')
#     if len(arr) > 1:
#         dict_.update({arr[0]: arr[1]})
#     elif len(arr) == 1:
#         print(dict_[arr[0]])
#     str_ = input()
dict_ = {}
str_ = input()
while str_ != '.':
    arr = str_.split(' ')
    dict.update({arr[0]: arr[-1:]})
    print(dict)
    str_ = input()