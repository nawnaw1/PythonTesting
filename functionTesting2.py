def do_calculation():
    command=input("Enter your command")
    print("lets " + command + " some numbers")
    input1 = input("Number 1>")
    input2 = input("Number 2>")
    number1 = int(input1)
    number2 = int(input2)
    if command == "+":
        result = number1 + number2
    elif command == "subtract":
        result = number1 - number2
    output = str(result)
    if command == "add":
        print(input1 + " + " + input2 + " = " + output)
    elif command == "subtract":
        print(input1 + " - " + input2 + " = " + output)
    else:
        print("This is the end")
do_calculation()