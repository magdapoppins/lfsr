def bitwise_add(a, b):
    # What to do if two arrays of not equal length?
    if (len(a) != len(b)):
        print("For now, lets have binaries of the same length.")

    answer = []
    for i in range(len(a)):
        currentIndex = len(a)-i-1
        answer.append(int(a[currentIndex] != b[currentIndex]))

    return answer[::-1]





        