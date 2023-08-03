def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s=s.lower()
    first_two_letters = s[0:2]
    if first_two_letters.isnumeric() or len(s) >  6 or len(s) < 2 or not s[-1].isnumeric()  or  is_first_int_zero(s) or is_special_char(s):
        return False
    return True

def is_first_int_zero(s):
    check = False
    for char in s:
        if char.isnumeric():
            if char == '0':
                check = True
                break
            else:
                break
    return check
def is_special_char(s):
    check = False
    for char in s:
        if char.isnumeric() or char.isalpha():
            continue
        else:
            check = True 
            break
    return check

main()
