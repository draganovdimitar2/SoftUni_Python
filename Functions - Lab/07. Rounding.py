def round_numbers(input_string):
    number_strings = input_string.split()
    rounded_numbers = [round(float(num)) for num in number_strings]
    return rounded_numbers


input_string = input()
print(round_numbers(input_string))