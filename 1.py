d_books = {}


def sort_rows(row):
    res = 0
    row = row.replace('Взять "', '').replace(')', '').replace('(', '').replace('Вернуть "', '')
    arr2 = row.split('" ')
    arr3 = arr2[1].split(' ')
    day, month, year = map(int, arr3[0].split('.'))
    res = year * 365 + month * 30 + day
    return res


def is_date_expire(d, d_current):
    # print(day, '\n', month, '\n',year)
    if not d:
        return True
    day, month, year = map(int, d.split('.'))
    day_c, month_c, year_c = map(int, d_current.split('.'))
    days = year * 365 + month * 30 + day
    days_c = year_c * 365 + month_c * 30 + day_c
    return day_c - days > 30


def take_book(s):
    s = s.replace('Взять "', '').replace(')', '').replace('(', '')
    book, other = s.split('" ')
    date, name = other.split(' ')
    reader_name = d_books.get(book).get('reader')
    if reader_name:
        reader_date = d_books.get(book).get('date', '')
        if is_date_expire(reader_date, date):
            d_books[book] = {'reader': name, 'date': date}
            print(f'Книгу "{book}" забрал(а) {name}')
        else:
            print(f'Книга "{book}" отсутствует. Ее забрал(а)', reader_name)
    else:
        d_books[book] = {'reader': name, 'date': date}
        print(f'Книгу "{book}" забрал(а) {name}')


def give_book_back(s):
    s = s.replace('Вернуть "', '').replace(')', '').replace('(', '')
    book, other = s.split('" ')
    d_books[book] = {'date': None, 'reader': None}

    # arr_books = input().replace('"', '').split(', ')
    # arr_books = '"Эдем", "Солярис", "Война и мир", "Честь имею", "Ночной дозор", "Оно"'.replace('"', '').split(', ')


arr_books = input().replace('"', '').split(', ')
for book_ in arr_books:
    d_books[book_] = {'reader': None, 'date': None}

s1 = input()
arr = []
while s1 != '.':
    arr.append(s1)
    s1 = input()
arr.sort(key=sort_rows)

for el in arr:
    if el.startswith('Взять'):
        take_book(el)
    if el.startswith('Вернуть'):
        give_book_back(el)
