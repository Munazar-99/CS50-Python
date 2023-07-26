expression = input('Expression: ')

match expression:
    case _ if '+' in expression:
        values = expression.split('+')
        print(float(values[0]) + float(values[1]))
    case _ if '-' in expression:
        values = expression.split('-')
        print(float(values[0]) - float(values[1]))
    case _ if '*' in expression:
        values = expression.split('*')
        print(float(values[0]) * float(values[1]))
    case _ if '/' in expression:
        values = expression.split('/')
        print(float(values[0]) / float(values[1]))
    case _:
        print('Expression does not contain any of the mathematical symbols')
