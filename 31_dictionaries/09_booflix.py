str1 = 'Булгаков "Собачье сердце" (сатира), Толкин "Властелин колец" (фэнтези), Дойл "Затерянный мир" (научная фантастика), Кристи "Десять негритят" (детектив), Кинг "Сияние" (ужасы), Дойл "Отравленный пояс" (научная фантастика), Лавкрафт "Зов Ктулху" (ужасы), Лутц "Изучаем Python" (учебная литература), Рао "C++ за 21 день" (ужасы), Толкин "Хоббит" (фэнтези), Дойл "Долина ужаса" (детектив), Кинг "Оно" (ужасы), Кристи "Убийство в доме викария" (детектив), Кинг "Противостояние" (ужасы), Вейер "Марсианин" (научная фантастика)'
# str1 = input()
arr = str1.split(', ')
d_books = {}
for el in arr:
    book, type = el.split(' "')[1].split('" ')
    type = type[1:-1]
    d_books[book] = type

d_readers = {}


def getFavoriteGenres(reader):
    reader_obj = d_readers.get(reader)
    arr2 = []
    if reader_obj:
        genres = reader_obj.get('genres')
        arr1 = list(genres.items())
        arr1.sort(key=lambda el1: el1[1], reverse=True)
        max_ = arr1[0][1]
        for el3 in arr1:
            if max_ == el3[1]:
                arr2.append(el3[0])
            else:
                break
    return arr2


def get_genre(book_name):
    return d_books.get(book_name)


def get_books_of_genres(genres):
    result = set()
    for genre in genres:
        for book_name, genre_name in d_books.items():
            if genre_name == genre:
                result.add(book_name)
    return result


def advice_book(s):
    reader_name = s.replace(')', '').replace('Посоветуй мне книгу (', '')
    #     тут мы получим рекомендации для этого пользователя - массив названий
    favorite_genres = getFavoriteGenres(reader_name)
    books_of_favorite_genres = get_books_of_genres(favorite_genres)
    reader_obj = d_readers.get(reader_name)
    if reader_obj:
        read_books = reader_obj.get('read_books')
        recommended_books = books_of_favorite_genres.difference(read_books)
        recommended_books = list(map(lambda el2: '"' + el2 + '"', list(recommended_books)))
        if len(recommended_books) > 0:
            print(*recommended_books, sep=', ')
        else:
            print("Список пуст")
    else:
        print("Список пуст")

def add_read(s):
    reader_name, book_name = s.split(' "')
    book_name = book_name.replace('"', '')
    d = d_readers.get(reader_name)
    if d:
        # модифицируем ридера и добавляем книгу
        read_books = d.get('read_books')
        read_books.add(book_name)
        d_genres_ = d.get('genres')
        genre = get_genre(book_name)
        g = d_genres_.get(genre)
        if g:
            d_genres_[genre] += 1
        else:
            d_genres_[genre] = 1
    else:
        d_readers[reader_name] = {
            'read_books': {book_name},
            'genres': {get_genre(book_name): 1}
        }


str2 = input()
while str2 != '.':
    if str2.startswith('Посоветуй мне книгу'):
        advice_book(str2)
    else:
        add_read(str2)
    str2 = input()

