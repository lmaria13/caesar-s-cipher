print("Давай я зашифрую твоё сообщение по технике Цезаря.")
alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюяабвгдеёжзиклмнопрстуфхцчшщъыьэюя' # алфавит введён в список два раза, так как при смещении на большой шаг алфавит начинается сначала
while True:
    message = (input("Напиши слово кириллицей.\n")).lower() # возводим всё сообщение в нижний регистр для проверки по списку
    for check in alphabet:
        if message.lower().find(check.lower()):
            break
while not is_cyrillic(message):
            print("Я не знаю такого алфавита.") # защита от введения неверной раскладки

def is_cyrillic(message):

input_str = "testtest test1"
def check_for_russian(string):
    alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о", "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    for one_char in string:
        if one_char in alphabet:
            return True
    return False

print(check_for_russian(input_str))


cypher = ''
print("Теперь надо придумать ключ.")
while True:
    key = int(input("Назови любое число от 1 до 32.\n"))
    if 0 < key < 33:
        break
    else:
        print("Такой ключ не подойдёт.") # защита от введения неверного ключа
for step in message:
    order = alphabet.find(step)
    new_order = order + key
    if step in alphabet:
        cypher += alphabet[new_order]
    else:
        cypher += step
answer = cypher.capitalize()
print(f"Зашифрованное послание — {answer}.")
