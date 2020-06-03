str1 = 'Булгаков "Собачье сердце" (сатира), Толкин "Властелин колец" (фэнтези), Дойл "Затерянный мир" (научная фантастика), Кристи "Десять негритят" (детектив), Кинг "Сияние" (ужасы), Дойл "Отравленный пояс" (научная фантастика), Лавкрафт "Зов Ктулху" (ужасы), Лутц "Изучаем Python" (учебная литература), Рао "C++ за 21 день" (ужасы), Толкин "Хоббит" (фэнтези), Дойл "Долина ужаса" (детектив), Кинг "Оно" (ужасы), Кристи "Убийство в доме викария" (детектив), Кинг "Противостояние" (ужасы), Вейер "Марсианин" (научная фантастика)'
arr = str1.split(', ')
d_books = {}
for el in arr:
    book, type = el.split(' "')[1].split('" ')
    type = type[1:-1]
    d_books[book] = type
# print(d_books)
d_books_ = {
    'Собачье сердце': 'сатира',
    'Властелин колец': 'фэнтези'
}

d_readers = {
    'Dontsova': {
        'red_books': {"Десять негритят", "5 негритят", "Собачье сердце"},
        'genres': {'детектив': 2, 'сатира': 1}
    }
}


def getFavouriteGenre(reader_obj):
    genres = reader_obj.get('genres')
    arr1 = list(genres.items())
    arr1.sort(key=lambda el1: el1[1], reverse=True)
    return arr1[0][0]


favorite_genre = getFavouriteGenre(d_readers['Dontsova'])
print(favorite_genre)
