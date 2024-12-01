# Создаем функцию single_root_words, которая принимает одно обязательное
# слово в параметр root_word, а далее неограниченную последовательность
# в параметр *other_words.
def single_root_words(root_word, *other_words): # 2. Создаем внутри функции single_root_words пустой список same_words,который будет пополняться нужными словами.
    same_words = []
    for word in other_words:                    # При помощи цикла for переберите предполагаемо подходящие слова.
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():  #Функция должна составить новый список same_words .......
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)