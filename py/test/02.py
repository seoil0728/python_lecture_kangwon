def calculator(str):
    operand1, operator, operand2 = str.split(" ")
    if(operand1.isdigit() and operand2.isdigit()):
        if(operator == "+"):
            result = int(operand1) + int(operand2)
            print(str + " = " + repr(result))
        elif (operator == "-"):
            result = int(operand1) - int(operand2)
            print(str + " = " + repr(result))
        elif (operator == "*"):
            result = int(operand1) * int(operand2)
            print(str + " = " + repr(result))
        elif (operator == "/"):
            result = int(operand1) / int(operand2)
            print(str + " = " + repr(result))
        else:
            print("Not supported operator")
    else:
        print("It is not digit")

print("Simple Calculator!")
ques = input("Enter your question (ex. 3 * 2): ")
calculator(ques)


