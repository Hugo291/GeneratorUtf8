from PIL import Image, ImageDraw, ImageFont

#the height of one line
line = 70

#width of image
width = 1200

#height of images
height = line * 2500

#font
Arial_ttf = 'ARIALUNI.TTF'

#Space between char
space = 10

#Create the image in memory
img = Image.new('RGB', (width, height), color='white')

#init the current count of char
current_index_letter = 0


#size police

min_size_police = 12
max_size_police = 40

for letter_index in range(0, 25000):

    #current char
    char = chr(letter_index)



    if char.isprintable() and char != ' ':

        print(letter_index,char)

        #The current letter witout undefined caracteres
        current_index_letter += 1

        #Between police_size min and max
        for size_Police in range(min_size_police, max_size_police):

            #Size of image
            #width = size_Of_Police * space_Between_Word*3
            #height = line_Height * count_index_letter
            size = ( ( (size_Police+space) + ( (size_Police - min_size_police)*space*4) ) + space , line * current_index_letter)

            #The font with the size
            font = ImageFont.truetype(font=Arial_ttf, size=size_Police)

            #add Font to text
            d = ImageDraw.Draw(img)

            #write in image
            d.text(size, char, font=font, fill=(0, 0, 0))

            #debug
            #print(chr(letter_index), 'size', size, 'police', size_Police)

#Save the image
img.save('image.png')

#show iamge
#img.show()
