list = open('text.txt').read().splitlines()


for row in list:
    row = int(row)
    for line in list:
        line = int(line)
        for element in list:
            element = int(element)
            if row + line + element == 2020:
                print(row)
                print(line)
                print(element)
