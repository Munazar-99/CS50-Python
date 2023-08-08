def main():
    fruits = {
        'Apple': 130,
        'Banana': 30,
        'Avacado': 50,
        'Sweet Cherries': 100,
    }
    fruit_chosen = input('Choose a fruit: ').capitalize()
    if fruit_chosen in fruits:
        print(fruits[fruit_chosen])
    else:
        print('Data not Available')

main()