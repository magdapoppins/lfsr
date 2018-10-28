# Sample of simple LFSR

def shift(startstate, tap_1, tap_2):
    counter = 0
    cipherbits = []
    register = startstate.copy()
    while (True):
        cipherbits.append(register[-1])
        counter += 1
        register = [(int(register[tap_1] != register[tap_2]))] + register[:-1]
        if register == startstate:
            break

    return cipherbits[::-1]

print(shift([0,1,0,1], 0, 2))