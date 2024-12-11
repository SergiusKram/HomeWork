# name = input('введите ваше имя : ')
# if name == 'Sergey':
#     print('Здравствуйте, администратор ')
# if name == 'Elya':
#     print('Здравствуйте, жена администратора!!!')
# else:
#     print('Привет', name)

number = int(input('Turm number'))
if number % 3 == 0 and number % 5 == 0:
    print('fizzBuzz')
# Fizz , Buzz , FizzBuzz
elif number % 3 == 0 :
    print('Fizz')
elif number % 5 == 0 :
    print('Buzz')
else:
     print('число не подходит')
