
def b_to_d():
    binary = False
    while binary == False:
        number_given = input("Binary number to convert: ")
        decimal_number = 0
        number_given = str(number_given)
        binary = True
        for i in number_given:
            if i != "0" and i != "1":
                binary = False
                print(f"The number {number_given} is not binary.")
    if binary:
        index = len(number_given) -1
        loop_count = -1
        while index != -1:
            loop_count += 1
            number_in_number_given = number_given[index]
            if number_in_number_given == "1":
                decimal_number += 2 ** loop_count
            index -= 1
        print(f"The number {number_given} is equivalent to {decimal_number} in the decimal system.")
    else:
        print("The number you gave is not binary.")



def d_to_b():
    righttype = False
    while righttype == False:
        given_number = input("Please give me a decimal number: ")
        try:
            given_number = int(given_number)
            righttype = True
        except:
            print("Please only enter numbers.")
    # the rest number is fistly equal to the number
    rest = given_number
    # binary num = lst 0000000000
    binary_number = []
    binary_sys = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    # while rest > 0for n in  the binary sys lst, if the decimal n is lower than n, binary num[loop count] = 1 and rest num -= n
    loop_count = 0
    while rest > 0:
        for n in binary_sys:
            if rest > 0:
                binary_number.append(0)
            if n <= rest:
                index = binary_sys.index(n)
                binary_number[index] = 1
                rest -= n
    for i in binary_number:
        if binary_number.index(n) > index:
            binary_number.remove(n)
    print(*binary_number)
def mode_asking():
    right_mode = False
    while right_mode == False:
        mode = input("Enter 'b to d' to convert from binary to decimal or 'd to b' to convert decimal to binary: ")
        mode = mode.lower()
        if mode == "b to d":
            b_to_d()
            right_mode = True
        elif mode == "d to b":
            d_to_b()
            right_mode = True
        else:
            print("Please enter something valid.")
mode_asking()

