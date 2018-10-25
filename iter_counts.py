# This code attempts to answer the question of how to select taps for the register
# in such a way that the produced loop is as long as possible.

def iter_amount(tapPositions, bitLength):
    register = generate_array(bitLength)
    print(register)
    original = register.copy()
    counter = 0
    while (True):
        shifted = register[0]
        # TODO: Let this xor the given taps (maybe for i in range(len(taps)))
        register[0] = int(register[0] != register[1])
        register[1] = shifted
        counter += 1
        if (register == original):
            break
    

    print("Finished, count of iterations was " + str(counter))



def generate_array(bitLength):
    arrayToReturn = []

    for pos in range(bitLength):
        arrayToReturn.append(1)

    return arrayToReturn


iter_amount([0, 1], 2)