# задача 3. Напишите программу, удаляющую из текста все слова содержащие "абв".

new_text = 'полученный текст без букв "абв"'

def del_some_words(new_text):
    new_text = list(filter(lambda x: 'абв' not in x, new_text.split()))
    return " ".join(new_text)

new_text = del_some_words(new_text)
print(new_text)