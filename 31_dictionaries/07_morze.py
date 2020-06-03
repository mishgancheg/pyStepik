morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
         'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
         's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
morze_rev = dict(zip(morze.values(), morze.keys()))
# str_ = input().lower()
tab = '\t'
res = []
str_ = '— •••• •	——•— ••— •• —•—• —•—	—••• •—• ——— •—— —•	••—• ——— —••—	•——— ••— —— •——• •••	——— •••— • •—•	— •••• •	•—•• •— ——•• —•——	—•• ——— ——•'.lower()
if str_.startswith('—') or str_.startswith('•'):
    words = str_.split('\t')
    array = []
    for word in words:
        chars_m = word.split()
        chars = list(map(lambda ch: morze_rev.get(ch, ''), chars_m))
        word_s = ''.join(chars)
        array.append(word_s)
    print(*array)
else:
    words = str_.split()
    morze_result = tab.join(map(lambda word: ' '.join(list(map(lambda ch: morze.get(ch, ''), list(word)))), words))
    print(morze_result)
