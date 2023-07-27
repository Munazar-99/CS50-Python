def main():
    given_input =input('String: ')
    print(remove_vowels(given_input))

def remove_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for char in words:
        if char not in vowels:
            result = result + char
    
    return result

if __name__ == "__main__":
    main()  
