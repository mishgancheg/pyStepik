code_dict = {}
coded_word = input()
code = list(coded_word)
for char in code:
    if not (char in ',. !?-'):
        if code_dict.get(char):
            code_dict[char] += 1
        else:
            code_dict[char] = 1
code_dict = dict(zip(code_dict.values(), code_dict.keys()))
words = input()
while words != '.':
    decoded_char, num = words.split(': ')
    coded_char = code_dict.get(int(num))
    coded_word = coded_word.replace(coded_char, decoded_char)
    words = input()
print(coded_word)
