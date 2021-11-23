
#task 2

you_number = input('Введіть номер: +380')
while True:
    if  len(you_number) == 9:
        print('Ваш номер: +380' + you_number)
        break
    elif len(you_number) != 9:
        you_number = input(str('Введіть номер: +380'))
    else:
        print('Ваш номер: +380' + you_number)
        break

#task 1

your_word = input('Введіть слово: ')
if len(your_word) == 2:
    print(your_word+your_word)
elif len(your_word) == 1:
    print()
elif len(your_word) == 4:
    print(your_word[0:2] + your_word[2:4])
elif len(your_word) == 5:
    print(your_word[0:2]+your_word[3:5])
elif len(your_word) == 5:
    print(your_word[0:2] + your_word[3:5])
elif len(your_word) == 6:
    print(your_word[0:2]+your_word[4:6])
elif len(your_word) == 7:
    print(your_word[0:2]+your_word[5:7])
elif len(your_word) == 8:
    print(your_word[0:2]+your_word[6:8])
else:
    print(your_word)


# task 3

name = 'діма'
name1 = input('')
while True:
    if name1 == name:
        print(name1.capitalize())
        break
    elif name1 != name:
        name1 = input('Введіть правильно ім`я ')
    else: print(name1.capitalize())








