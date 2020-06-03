str_ = input().replace(',', '')
dict = {}
while str_ != '.':
    arr = str_.split(' ')
    if len(arr) == 1:
        if (dict.get(arr[0])) and (len(dict.get(arr[0])) == 11) and (dict.get(arr[0].startswith('+7')) or dict.get(arr[0].startswith('8'))):
            print(*dict.get(arr[0], []), sep=', ')
        else:
            print('Не найдено')
    else:
        dict[arr[0]] = dict.get(arr[0], []) + arr[1:]
    str_ = input().replace(',', '')
