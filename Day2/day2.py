data = open('text.txt').read()


def splitter(number):
    splitted_data = data.split()
    row = (number - 1) * 3
    required_amount_from = splitted_data[row].partition("-")[0]
    required_amount_to = splitted_data[row].partition("-")[2]
    required_letter = splitted_data[row + 1][0]
    password = splitted_data[row + 2]
    return required_amount_from, required_amount_to, required_letter, password

count = 0
for x in range(1000):
    required_amount_from, required_amount_to, required_letter, password = splitter(x)
    required_letter_in_password = password.count(required_letter)
    if required_letter_in_password in range(int(required_amount_from), int(required_amount_to) + 1):
        count += 1

print(count)


count = 0
for x in range(1000):
    required_amount_from, required_amount_to, required_letter, password = splitter(x)
    if (required_letter == password[int(required_amount_from) - 1] and not required_letter == password[int(required_amount_to) - 1]) or \
            (not required_letter == password[int(required_amount_from) - 1] and required_letter == password[int(required_amount_to) - 1]):

        count += 1
print(count)
