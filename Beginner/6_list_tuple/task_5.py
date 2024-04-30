words = input("Vergul bilan ajratib so'zlar kiriting:  ").split(sep=",")
print(words)
searching_word = input('qidirayotgan sozingizni kiriting:  ')

amount = words.count(searching_word)
print(amount)