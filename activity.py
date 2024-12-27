def decimal_to_binary(n):
    binary_num = []
    while n > 0:
        binary_num.append(n % 2)
        n = n // 2
    
    
    binary_num.reverse()
    
    
    binary_str = ''.join(str(bit) for bit in binary_num)
    return binary_str


decimal_number = int(input("Enter any number: "))
binary = decimal_to_binary(decimal_number)
print( decimal_number, "in binary form is", binary)