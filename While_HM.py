my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0

while initial_value < len(my_list):

    if my_list[initial_value] == 0: # проверяю, равно ли число нулю
        initial_value += 1   # увеличиваю индекс
        continue # перехожу к следующей итерации

    if my_list[initial_value] < 0: # проверяю на отрицательные числа
       break   # прерываю выполнение цикла

    print(my_list[initial_value]) # вывожу положительное число
    initial_value += 1 # увеличиваю индекс


