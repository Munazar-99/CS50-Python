def main():
    convert()

def convert():
    final_emojis = input('Insert sentences with emoticon ').replace(':)', '🙂').replace(':(', '🙁')
    print(final_emojis)

main()