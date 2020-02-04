def user_input():
    polska_strong = input().split()
    operand = polska_strong[0]
    num1 = polska_strong[1]
    num2 = polska_strong[2]
    result = polska_strong[1] + operand + polska_strong[2]
    assert operand in ['+', '-', '/', '*'], 'Наша версия программы пока не поддерживает такой операнд'
    if len(polska_strong) > 3:
        print('Мы ждали операнд и 2 элемента, попробуем снова..')
        user_input()
    return result


while True:
    try:
        result = user_input()
        print(eval(result))
    except ZeroDivisionError:
        print('Очень жаль что нельзя делить на ноль. Попробуйте снова')
    except NameError:
        print('Со строками так нельзя, окститесь!')
    except IndexError:
        print('Введено неверное колличество элементов')
    except:
        print('От всех ошибок никто не застрахован. У нас тут "Голое исключение" - завершаем')
        break
    else:
        break
