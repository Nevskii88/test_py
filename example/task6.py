# some_list = [1, 2, 3, 4, 5, 6]
# with open('result.txt', 'w', encoding='utf-8') as file:
# for el in some_list:
# file.write(str(el) + '\n')

# with open('example.txt', 'r', encoding='utf-8') as file:
# text_list = file.read().splitlines()
# first_len = len(text_list[0])
# result_list = [i for i in text_list if len(i) == first_len]
# with open('result.txt', 'w', encoding='utf-8') as res:
# for el in result_list:
# res.write(el + '\n')

# Напишите функцию read_last(lines, file), 
# которая будет открывать определенный файл file 
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, 
# что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым

with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)