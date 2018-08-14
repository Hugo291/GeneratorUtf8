from generator import draw, get_number

if __name__ == '__main__':
    print("Please enter the first utf-8 number : ")
    first_char_utf_8_number = get_number()

    print("Please enter the last utf-8 number : ")
    last_char_utf_8_number = get_number()

    print(draw(first_char_utf_8_number, last_char_utf_8_number))
