def print_file_lines(filename):
    with open(filename, "r") as file:

        lines = file.readlines()

        print("This file has {} lines" .format(len(lines)))

        while True:
            line_num = input ("Enter a line number (0 to quit): ")

            line_num = int(line_num)

            if line_num == 0:
                break

            if line_num < 1 or line_num > len(lines):
                print("Invalid line number. Please enter a number between 1 and {}." .format(len(lines)))  
                continue

            print("Line {}: {}" .format(line_num, lines[line_num - 1]))    

    filename = input('Enter a filename: ')      
    
    print_file_lines(filename)
        