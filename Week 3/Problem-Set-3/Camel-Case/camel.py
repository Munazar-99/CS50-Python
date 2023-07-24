def main():
    camel_case = input('Camel Case: ')
    print(camel_to_snake(camel_case))


def camel_to_snake(word):
    snake_case = ''
    for char in word:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()    