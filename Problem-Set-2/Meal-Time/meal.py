def main():
    time_given = input('What time is it? ')
    numerized_time = convert(time_given)
    match numerized_time:
        case _ if numerized_time >= 7.0 and numerized_time <= 8.0:
            print('its breakfast time')
        case _ if numerized_time >= 12.00 and numerized_time <= 13.00:
            print('its lunch time')
        case _ if numerized_time >= 18.00 and numerized_time <= 19.00:
            print('its dinner time')

def convert(time):
    return float(time.replace(':', '.'))


if __name__ == "__main__":
    main()