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
