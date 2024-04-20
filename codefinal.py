print("Давай я зашифрую твоё сообщение по технике Цезаря.")
alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюяабвгдеёжзиклмнопрстуфхцчшщъыьэюя' # алфавит введён в список два раза, так как при смещении на большой шаг алфавит начинается сначала
def is_cyrillic(text):
    for char in text:
        if not ('а' <= char <= 'я' or 'А' <= char <= 'Я' or char == 'ё' or char == 'Ё'):
            return False
    return True

def get_cyrillic_input(prompt):
    while True:
        user_input = input(prompt)
        if is_cyrillic(user_input):
            return user_input
        else:
            print("Пожалуйста, введите только символы кириллицы.")
            
message = get_cyrillic_input("Введите текст кириллицей.\n").lower()

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

