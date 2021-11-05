def hash_function(mes):
    new_hash = ""
    total_number = 0
    number2 = 0
    for i in mes:
        total_number += int(ord(i)) // len(mes)
    # print(f"Total number = {total_number}")
    for i in mes:
        number = int(ord(i))  # Возвращает числовое представление для указанного символа
        number = int((number ** len(mes)) // len(mes))  # математические преобразование с числом относительно длины message
        j = 1
        while number:
            first = number // 3
            number2 += first * j    # наращиваем n2 относительно n//3
            j *= 10
            number //= 10
        # print(f"number2 = {number2}")
        arr = list(str(number2))
        for counter in range(total_number):  #переставляем местами total_number раз
            arr.insert(0, arr.pop())
        new_hash += "".join(arr)  # создаем результирующую строку
    return new_hash


while True:
    message = input("\nВведите \"000\" для выхода\nВведите сообщение для хэширования: ")
    if message == "000":
        print("\nEXIT...")
        break
    else:
        hash_m = hash_function(message)
        print(f"Хэш-код: {hash_m}")
