words = input("Vergul bilan ajratib so'zlar kiriting:  ").split(sep=",")
searching_word = input('qidirayotgan sozingizni kiriting:  ')

index = words.index(searching_word)
print(index)