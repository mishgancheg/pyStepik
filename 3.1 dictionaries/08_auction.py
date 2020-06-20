line1 = input()
startPrice = int(input())
users = {}
for el in input().split(', '):
    users[el] = 'есть'
arr = line1.split(', ')
dict_ = {}
for el in arr:
    dict_[el] = {'price': startPrice, 'person': None}
str_ = input()
while str_ != 'Аукцион закончен!':
    item = str_.split(' ')
    price = int(item[-1:][0])
    person = item[0:1][0]
    item = ' '.join(item[1:-1])
    if price > dict_.get(item).get('price') and users.get(person):
        dict_[item] = {'price': price, 'person': person}
    str_ = input()
for item, info in dict_.items():
    if info.get('person'):
        print(item, info.get('person'), info.get('price'))
    else:
        print(item, 'Предложений не было')


