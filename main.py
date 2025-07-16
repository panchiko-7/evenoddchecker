num = input('enter a number and i will guess if its odd or even mwahahaha: ')

if '.' in num:
    print('this is a decimal')
else:
    try:
        num = int(num)
        if num % 2 == 0:
            print('this is even me thinks')
        else:
            print('this is odd me thinks')
    except ValueError:
        print('this is not a valid number me thinks')