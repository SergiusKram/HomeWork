numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for j in numbers:
    if j == 1:                # Пропускаем число 1
        continue

    is_prime = True           # число простое

    for i in range(2, j):      # проверка делимости в диапазоне с 2 до 9 (j-1)
        if j  % i == 0:
           is_prime = False   # число не простое
           break

    if is_prime:
       primes.append(j)           # добавляем в список простых числел
    else:
       not_primes.append(j)        # добавляем в список непростых чисел
print('Primes:', primes)
print('Not Primes:', not_primes)
