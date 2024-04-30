words = input('sozlarni kiriting:  ').split(sep=' ')

word_1 = sorted(words[0].lower())
word_2 = sorted(words[1].lower())
true_false = True

if not word_1 == word_2:
    true_false = False
else:
    true_false = True

print(true_false)