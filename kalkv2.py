print("Доброго времени суток, я калькулятор и я готов решать ваши проблемы")
print("Для начала определимся с количеством действий")
count = int(input())
while count >= 1:
    print(f"Выполняем операцию под номером {count}")
    print("Введите первое число")
    nomer1 = float(input())
    print(
        "Выберите действие: 1-Сложение 2-Вычитание 3-Умножение 4-Деление 5-Возведение в степень \nОпределись с операцией, которую тебе надо выполнить и введи её число на клавиатуре")
    do = int(input())
    if do == 1:
        print("Введите второе число")
        nomer2 = float(input())
        result = nomer1 + nomer2
    elif do == 2:
        print("Введите второе число")
        nomer2 = float(input())
        result = nomer1 - nomer2
    elif do == 3:
        print("Введите второе число")
        nomer2 = float(input())
        result = nomer1 * nomer2
    elif do == 4:
        print("Введите второе число")
        nomer2 = float(input())
        while(nomer2==0):
            print("Делить на ноль нельзя")
            print("Введите второе число")
            nomer2 = float(input())
        else:
            result = nomer1 / nomer2
    elif do == 5:
        print("Введите второе число")
        nomer2 = float(input())
        result = nomer1 ** nomer2
    else:
        print("Неверное число. Выбери операцию из тех, которые представлены выше")
        exit()
    print(f"Ответик: {result}")
    count = count - 1
    nomer2=0

print("Закончили работу")
