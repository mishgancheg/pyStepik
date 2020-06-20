str_ = input()
countries = {}
capitals = {}
while str_ != '.':
    arr = str_.split(': ')
    countries.update({arr[0]: arr[1]})
    capitals.update({arr[1]: arr[0]})
    str_ = input()
str_ = input()
while str_ != '.':
    if countries.get(str_):
        print(countries[str_])
    elif capitals.get(str_):
        print(capitals[str_])
    else:
        print('Нет данных')
    str_ = input()