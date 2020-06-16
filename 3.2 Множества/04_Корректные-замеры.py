set1 = set(input().split())
set2 = set(input().split())
if len(set1.intersection(set2)) / len(set1) > 0.7:
    print('Корректно')
else:
    print('Некорректно')