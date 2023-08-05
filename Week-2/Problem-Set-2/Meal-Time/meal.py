def main():
    time_given = input('What time is it? ')
    numerized_time = convert(time_given)
    
    if 7.0 <= numerized_time <= 8.0:
        print('It\'s breakfast time')
    elif 12.0 <= numerized_time <= 13.0:
        print('It\'s lunch time')
    elif 18.0 <= numerized_time <= 19.0:
        print('It\'s dinner time')
    else:
        print('Not meal time')

def convert(time):
    return float(time.replace(':', '.'))

if __name__ == "__main__":
    main()
