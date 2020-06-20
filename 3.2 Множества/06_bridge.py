x = int(input())
know_next = set()
know_everybody = set()
for i in range(x):
    if i == 0:
        know_everybody = set(input().split(', '))
    else:
        know_next = set(input().split(', '))
        know_everybody = know_everybody.intersection(know_next)

if len(know_everybody):
    print(*know_everybody, sep=', ')
else:
    print('Фильм снять не удастся:(')


