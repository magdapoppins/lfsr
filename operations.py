def add(a, b, out='str'):
    # Takes two binary strings and bitwise XOR's them
    res_int = operate(a, b, add_func)  # Convert to int using base 2 and bitwise XOR
    return convert_output(res_int, out, 0)


def bitwise_xor(a, b, out='str', pad=True):
    # Takes two binary strings and bitwise XOR's them
    res_int = operate(a, b, xor_func)  # Convert to int using base 2 and bitwise XOR
    if pad:
        padded_len = max(len(a), len(b))
    else:
        padded_len = 0
    return convert_output(res_int, out, padded_len)


def bitwise_and(a, b, out='str', pad=True):
    # Takes two binary strings and bitwise XOR's them
    res_int = operate(a, b, and_func)  # Convert to int using base 2 and bitwise XOR
    if pad:
        padded_len = max(len(a), len(b))
    else:
        padded_len = 0
    return convert_output(res_int, out, padded_len)


def convert_output(int_val, out='str', padded_len=0):
    if out not in ['str', 'int', 'int[]']:
        raise ValueError("illegal 'out' parameter, allowed: ['str', 'int', 'int[]']")
    if out == 'int':
        return int_val
    else:
        res_str = "{0:b}".format(int_val)  # Convert int to binary representation
        if padded_len > len(res_str):
            res_str = res_str.zfill(padded_len)  # Pad up to the length of the larger input. Does not imply significant bits!
        if out == 'str':
            return res_str
        if out == 'int[]':
            return bin_str2int_arr(res_str)


def xor_func(x, y):
    return x ^ y


def and_func(x, y):
    return x & y


def add_func(x, y):
    return x + y


def operate(a, b, func):
    return func(int(a, 2), int(b, 2))  # Convert to int using base 2 and use the lambda function


def bin_str2int_arr(bin_str):
    arr = []
    for bit in bin_str:
        arr.append(int(bit))
    return arr
