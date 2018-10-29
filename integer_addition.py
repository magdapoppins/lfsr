def add_bin(a, b):
    # Takes two binary strings and adds them
    res_add = int(a, 2) + int(b, 2)  # Convert to int with base 2 and add
    res_str = "{0:b}".format(res_add)  # Convert int to binary string
    return res_str

def integer_add(a, b):
    carry = 0
    # TODO: What to do if two arrays of not equal length?
    # TODO: Result can be longer than params :_D
    if (len(a) != len(b)):
        print("For now, lets have binaries of the same length.")
    
    answer = []
    for i in range(len(a)):
        index = len(a)-i-1
        if (a[index] == "1" and b[index] == "1"):
            carry = 1
            result = 0
        else:
            result = use_carry(int(a[index] != b[index]), carry)
        answer.append(result)
    
    return answer[::-1]

def use_carry(bit_value, carry):
    # If 0, just return 1 and set carrier to 0
    # If 1 return 0 and reset carrier to 1
    if carry == 0:
        return bit_value
    if bit_value == 0:
        return 1
        carry = 0
    elif bit_value == 1:
        return 1    
