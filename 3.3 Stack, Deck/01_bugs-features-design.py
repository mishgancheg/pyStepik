bugs = []
features = []
design = []
str_ = input()
while str_ != 'Релиз!':
    if str_.startswith('Добавить '):
        if 'bugs' in str_:
            other, bug = str_.split(': ')
            bugs.append(bug)
        elif 'features' in str_:
            other, feature = str_.split(': ')
            features.append(feature)
        elif 'design' in str_:
            other, design1 = str_.split(': ')
            design.append(design1)
    elif str_.startswith('Убрать '):
        if 'bugs' in str_:
            bugs.remove(bugs[-1])
        elif 'features' in str_:
            features.remove(features[-1])
        elif 'design' in str_:
            design.remove(design[-1])
    str_ = input()
if len(bugs) == 0:
    print('Все исправлено!')
else:
    print(bugs[-1])
if len(features) == 0:
    print('Все исправлено!')
else:
    print(features[-1])
if len(design) == 0:
    print('Все исправлено!')
else:
    print(design[-1])
