def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_two_letters = s[0:2]
    if first_two_letters.isnumeric():
        return False
    


main()
