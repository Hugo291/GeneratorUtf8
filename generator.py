from PIL import Image, ImageDraw, ImageFont



def draw(first_char_utf_8_number : int, last_char_utf_8_number:int, debug = False, file_name = 'image.png'):

	number_lines = get_image_height(first_char_utf_8_number , last_char_utf_8_number)

	#the height of one line in px
	line = 70

	last_char_utf_8_number = last_char_utf_8_number+1

	#width of image in px
	width = 1200

	#height of images 
	height = line * (number_lines+1)

	#font
	Arial_ttf = 'ARIALUNI.TTF'

	#Space between chars
	space = 10

	#Create the image in memory
	img = Image.new('RGB', (width, height), color='white')

	#init the current count of char
	current_char_index = 0

	#size police
	min_police_size = 12
	max_police_size = 40

	for letter_index in range(first_char_utf_8_number, last_char_utf_8_number):

		#current char
		char = chr(letter_index)

		if char.isprintable() and char != ' ':

			print("char = ",chr(letter_index) , '\t utf-8 number : ',letter_index) 

			#Between police_size min and max
			for size_Police in range(min_police_size, max_police_size):

				#Size of image
				size = ( ( (size_Police+space) + ( (size_Police - min_police_size)*space*4) ) + space , line * current_char_index)

				#The font with the size
				font = ImageFont.truetype(font=Arial_ttf, size=size_Police)

				#add Font to text
				d = ImageDraw.Draw(img)

				#write in image
				d.text(size, char, font=font, fill=(0, 0, 0))

				#debug
				if debug == True:
					print('position = ', size, '\t police size  = ', size_Police)

			current_char_index += 1
	
	#Save the image
	img.save(file_name)

def get_number() -> int:
	try :
		return int(input())
	except Exception:
		print("Please enter a number : ")
		get_number()

def get_image_height(first_char_utf_8_number , last_char_utf_8_number):
	return last_char_utf_8_number - first_char_utf_8_number

if __name__ == '__main__':
	
	print("Please enter the first utf-8 number : ")
	first_char_utf_8_number = get_number()

	print("Please enter the last utf-8 number : ")
	last_char_utf_8_number = get_number()

	draw( first_char_utf_8_number, last_char_utf_8_number)