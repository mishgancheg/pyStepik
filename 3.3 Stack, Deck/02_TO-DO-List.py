
n = int(input())
dict_ = {}
complete = []
for i in range(n):
    str_ = input()
    if str_.startswith('Добавить:'):
        str_ = str_[10:]
        act, time = str_.split('. ')
        dict_[act] = time
    if str_.startswith('Выполнить:'):
        str_ = str_[11:]
        act, time = str_.split('. ')
        complete.append(act)
a_deals = list(dict_.items())
a_deals.sort(key=lambda el: el[1], reverse=True)
for key in list(dict_.keys()):
    for act in complete:
        if key == act and dict_.get(act):
            del dict_[act]
if len(dict_) == 0:
    print("Все выполнено!")
else:
    print(*dict_, sep=', ')

