number_given = input("Binary number to convert: ")
decimal_number = 0
number_given = str(number_given)
binary = True
for i in number_given:
    if i != "0" and i != "1":
        print(f"{i} is neither 1 nor 2")
        binary = False
if binary:
    index = len(number_given) -1
    loop_count = -1
    while index != -1:
        loop_count += 1
        number_in_number_given = number_given[index]
        if number_in_number_given == "1":
            decimal_number += 2 ** loop_count
        index -= 1
    print(decimal_number)
else:
    print("The number you gave is not binary.")

