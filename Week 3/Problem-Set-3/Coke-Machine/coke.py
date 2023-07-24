def main():
    amount_due = 50
    while True:
        if amount_due <= 0:
            print(f'Change Owed {abs(amount_due)}')
            break
        print(f'Amount Due {amount_due}')
        inserted_money = input('Insert Coin: ')
        match inserted_money:
            case '25':
                amount_due = amount_due - 25
            case '10':
                amount_due = amount_due - 10
            case '5':
                amount_due = amount_due - 5
            case _:
                print('Invalid coin')

if __name__ == "__main__":
    main()  


