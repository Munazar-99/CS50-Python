def main():
    amount_due = 50
    coin_values = {'25': 25, '10': 10, '5': 5}

    while amount_due > 0:
        print(f'Amount Due {amount_due}')
        inserted_money = input('Insert Coin: ')

        if inserted_money in coin_values:
            print (coin_values[inserted_money], 'munazar')
            amount_due -= coin_values[inserted_money]
        else:
            print('Invalid coin')

    print(f'Change Owed {abs(amount_due)}')

if __name__ == "__main__":
    main()
