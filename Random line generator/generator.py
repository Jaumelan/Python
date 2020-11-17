from PIL import Image, ImageDraw
from random import randint, shuffle


def random_color():
    rgbl=[250, 0, 0]
    shuffle(rgbl)
    return tuple(rgbl)

def nums_generate():
	x_first = randint(1, 1000)
	y_first = randint(1, 1000)
	x_second = randint(1, 700)
	y_second = randint(1, 700)
	return x_first, y_first, x_second, y_second

def rand_draw(val):
	img = Image.new('RGBA', (1000, 700), 'gray')
	n = 0
	while n < val:
		n += 1
		print(n)
		#print(nums_generate())
		#print(random_color())
		draw = ImageDraw.Draw(img)
		draw.line((nums_generate()), fill=random_color())
		img.save('i_draw.png')

	img.show()


my_value = int(input('enter how many you want a lines: '))

rand_draw(my_value)
