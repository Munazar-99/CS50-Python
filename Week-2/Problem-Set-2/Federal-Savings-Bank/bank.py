greeting = input('Greeting: ')

if greeting.lower().startswith('hello'):
    print('$0')
elif greeting.lower().startswith('h') and not greeting.startswith('hello'):
    print('$20')
else:
    print('$100')