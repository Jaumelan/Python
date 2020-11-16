file_name = 'some.txt'

with open(file_name, 'w+') as file_object:
	content = file_object.read()

	char_find = str(input('Enter char for find: '))
	char_change = str(input('Enter char for change: '))
	new_content = ''


	for text_line in content:
		if text_line != char_find:
			new_content += text_line

		else:
			new_content += char_change


new_name_file = 'changed_' + file_name

with open(new_name_file, 'w') as new_file:
	new_file.write(new_content)
