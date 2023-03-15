# Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).

# def read_last(lines, file):
#     if lines > 0:
#         with open('article.txt', 'r', encoding ='utf-8') as file:
#             text_list = file.readlines()[-lines:]
#         for line in text_list:
#             print(line)
#     else:
#         print('Количество строк может быть только положительным')

# read_last(5, 'article.txt')


# Требуется реализовать функцию longest_words(file),
# которая записывает в файл result.txt слово, имеющее максимальную длину 
# (или список слов, если таковых несколько).

# def longest_words (file):
#     with open('article.txt', 'r', encoding ='utf-8') as file:
#         text_list = file.read().split()
#         max_len = len(max(text_list, key = len))
#         words = str()
#         for word in text_list:
#             if len(word) == max_len:
#                 words += word + "\n"
#                 with open("result.txt", 'w', encoding ='utf-8') as file:
#                     file.write(words)
                
# longest_words('article.txt')


