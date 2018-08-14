from PIL import Image, ImageDraw, ImageFont


def draw(first_char_number: int, last_char_number: int, file_name='image.png', debug=False, ):
    """
    Draw image with all character between two value
    :param first_char_number: First number of character to be generated
    :param last_char_number: Last character to be generated
    :param debug: Boolean that enable the user to display all log during process
    :param file_name: The file name for the output file
    :return: dict of all character generated and their position in the image
    """
    number_lines = get_image_height(first_char_number, last_char_number)

    # the height of one line in px
    line = 70

    last_char_number = last_char_number + 1

    # width of image in px
    width = 1200

    # height of images
    height = line * (number_lines + 1)

    # font
    police_ttf = 'ARIALUNI.TTF'

    # Space between chars
    space = 10

    # Create the image in memory
    img = Image.new('RGB', (width, height), color='white')

    # init the current count of char
    current_char_index = 0

    # size police
    min_police_size = 12
    max_police_size = 25

    dict_char = {}

    for letter_index in range(first_char_number, last_char_number):

        list_positions = []

        # current char
        char = chr(letter_index)

        if char.isprintable() and char != ' ':

            dict_char[char] = list_positions

            print("char = ", chr(letter_index), '\t utf-8 number : ', letter_index)

            # Between police_size min and max
            for size_Police in range(min_police_size, max_police_size):

                # position char
                position_x = ((size_Police + space) + ((size_Police - min_police_size) * space * 4)) + space
                position_y = line * current_char_index

                # tuple size
                size = (position_x, position_y)

                # The font with the size
                font = ImageFont.truetype(font=police_ttf, size=size_Police)

                # add Font to text
                d = ImageDraw.Draw(img)

                # write in image
                d.text(size, char, font=font, fill=(0, 0, 0))

                # debug
                if debug:
                    print('position = ', size, '\t police size  = ', size_Police)

                list_positions.append(size)
            current_char_index += 1

    # Save the image
    img.save(file_name)

    return dict_char


def get_number() -> int:
    """
    This recursive function return a integer.
    :return: Int input enter by user
    """
    try:
        return int(input())
    except Exception:
        print("Please enter a number : ")
        get_number()


def get_image_height(first_char_number, last_char_number):
    """
    Return the image height with the
    :param first_char_number:
    :param last_char_number:
    :return:
    """
    return last_char_number - first_char_number
