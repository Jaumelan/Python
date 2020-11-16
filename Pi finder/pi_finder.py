# pi finder by Petryk

def get_value():
 	while True:
 		try:
 			find_value = int(input('Enter value for finding: '))
 			break

 		except ValueError:
 			print('Enter only integer')

 	return find_value


def find_value():
	file_name = 'pi_value.txt'

	with open(file_name, 'r') as pi_object:
		pi_value = pi_object.read()

		find_value = str(get_value())

		l_shift = 0
		r_shift = len(find_value)
		found = 0

		while l_shift < len(pi_value):
			pi_item = pi_value[l_shift : r_shift]
			l_shift += 1
			r_shift += 1

			if pi_item == find_value:
				found = pi_item
				print('Your value is ' + str(l_shift) + ' positions among ' + str(len(pi_value)) + ' values of the number pi')
				break

		if found == 0:
			print('Your number is not in pi value')


find_value()
