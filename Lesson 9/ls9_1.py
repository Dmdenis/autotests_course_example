# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


with open("test_file/task1_data.txt", mode='r', encoding='utf-8') as file:
    string = file.read()
new_string = []
for symbol in string:
    if not symbol.isdigit():
        new_string.append(symbol)
new_string = ''.join(new_string).strip()
f = open("test_file/task1_answer.txt", 'w', encoding='utf-8')
f.write(new_string)
f.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
