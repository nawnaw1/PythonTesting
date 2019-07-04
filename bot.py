print("I am personal robot for you, Naw")
print("What can i do for you to calculate Maths")

finish=False
while finish==False:
    print("Plase input two numbers for operations")
    input1 = input("Number 1> ")
    number1=int(input1)
    input2 = input("Number 2> ")
    number2=int(input2)
    command= input("Please give me some instruction for arithmetic operators (+,-,*,/) or bye for stop")
    if(command=="+"):
        result = number1 + number2
    elif(command=="-"):
        result = abs(number1 - number2)
    elif command == "average":
        how_many = input("How many numbers> ")
        how_many = int(how_many)
        total = 0
        #for number_count in range(how_many):
            #number = input("Enter number " + str(number_count) + "> ")
            #total = total + int(number)
            #result = total / how_many
            #print("the average = " + str(result))
    elif command=="bye":
        finish=True
    else:
        print("I don't understand your command")

