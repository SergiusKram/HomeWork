first = int(input('entering the first number'))
second = int(input('entering the second number'))
third = input('entering the third number')
if first == second == third :
    print(3,' All numbers are equal.',sep=',')
elif first == second or third == second or first == third :
    print(2,' Two numbers of three are equal to each other.',sep=',')
else :
    print(0, ' No equal numbers observed.',sep=',')
