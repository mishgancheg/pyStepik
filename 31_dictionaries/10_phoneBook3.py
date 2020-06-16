def check_and_add_numbers(d_phone_book_, name_, s_phones_):
    a_phones = s_phones_.split(', ')
    for i in range(len(a_phones)):
        phone = a_phones[i]
        if phone[0] == '8':
            phone = phone[1:]
        elif phone.startswith('+7'):
            phone = phone[2:]
        else:
            phone = ''

        phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        if len(phone) == 10 and phone.isdigit():
            phone = '+7 (' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10]
            if d_phone_book_.get(name_):
                d_phone_book_[name_].append(phone)
            else:
                d_phone_book_[name_] = [phone]


d_phone_book = {}
str_ = input()
while str_ != '.':
    arr = str_.split()
    name = arr[0]
    if len(arr) < 2:
        # запрос номеров
        phones = d_phone_book.get(name, [])
        if len(phones):
            print(*phones, sep=', ')
        else:
            print('Не найдено')

    else:
        # Ввод номеров
        s_phones = str_[len(name) + 1:]
        check_and_add_numbers(d_phone_book, name, s_phones)

    str_ = input()
