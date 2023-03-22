def string_with_big_letter(string):
    """
    Функция возвращает строку со всеми заглавными буквами
    """
    return string.upper()


def string_with_one_letter(string):
    """
    Функция, которая возвращает буквы каждого слова в строке
    """
    return string.title()


string = input("Введите строку ")

print(string_with_big_letter(string))
print(string_with_one_letter(string))
