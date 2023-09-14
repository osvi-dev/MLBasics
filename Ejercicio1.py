def number_to_binary(number:int) -> str:
    binary = ''
    if number == 0:
        return '0'
    
    while number > 0:
        binary = str(number%2) + binary
        number //=2 
    return binary

print(number_to_binary(100))