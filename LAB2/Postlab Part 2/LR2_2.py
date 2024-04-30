input_file = input('Enter the file name: ')

file_list = []

with open(input_file) as file:
    for line in file:
        file_list.append(line.strip())

    file_length = len(file_list)

checker = True

while checker:

    print('Number of lines: ', file_length)

    line_number = int(input('Please enter a line number (0 to exit): '))

    if line_number == 0:
        checker = False

    elif 1 <= line_number <= file_length:
        print(f'Line {line_number}: {file_list[line_number - 1]}\n')

    else:
        print(f'Invalid line number: {line_number}\n')
