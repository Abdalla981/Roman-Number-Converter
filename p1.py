def roman_number(user_input):
    if user_input > 9999 or user_input < 1:
        return 'Number is out of range'
    roman_string = ''
    user_input = str(user_input)
    user_input = list(user_input)
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    if len(user_input) == 4:
        roman_string += 'M'*int(user_input[0])
        del user_input[0]
    if len(user_input) == 3:
        roman_string += hundreds[int(user_input[0])]
        del user_input[0]
    if len(user_input) == 2:
        roman_string += tens[int(user_input[0])]
        del user_input[0]
    if len(user_input) == 1:
        roman_string += ones[int(user_input[0])]
        del user_input[0]
    return roman_string   
