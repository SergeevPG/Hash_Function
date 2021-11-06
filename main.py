def hash_function(mes):
    new_hash = ""
    total_number = 0
    number2 = 0
    # Суммируем числовое представление всех указанных символов
    for i in mes:
        total_number += int(ord(i)) // len(mes)
    # print(f"Total number = {total_number}")
    for i in mes:
        number = int(ord(i))  # Возвращает числовое представление для указанного символа
        number = int((number ** len(mes)) // len(mes))  # математические преобразование с числом относительно длины message
        j = 1
        # формируем новое число number2 относительно предыдущего number
        while number:
            first = number // 3
            number2 += first * j
            j *= 10
            number //= 10
        # print(f"number2 = {number2}")
        # создаем массив из получившегося числа
        arr = list(str(number2))
        # переставляем местами цифры в новом числе для лучшей шифровки
        for counter in range(total_number):
            arr.insert(0, arr.pop())
        # создаем результирующую строку
        new_hash += "".join(arr)
    return new_hash


while True:
    message = input("\nВведите \"000\" для выхода\nВведите сообщение для хэширования: ")
    if message == "000":
        print("\nEXIT...")
        break
    else:
        hash_m = hash_function(message)
        print(f"Хэш-код: {hash_m}")
