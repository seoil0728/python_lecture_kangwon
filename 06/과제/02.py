def calculator(strs):
    operand1, operator, operand2 = strs.split(" ")
    if(operand1.isdigit() and operand2.isdigit()):
        if(operator == "+"):
            result = int(operand1) + int(operand2)
            print(strs + " = " + str(result))
        elif (operator == "-"):
            result = int(operand1) - int(operand2)
            print(strs + " = " + str(result))
        elif (operator == "*"):
            result = int(operand1) * int(operand2)
            print(strs + " = " + str(result))
        elif (operator == "/"):
            result = int(operand1) / int(operand2)
            print(strs + " = " + str(result))
        else:
            print("Not supported operator")
    else:
        print("It is not digit")

print("Simple Calculator!")
ques = input("Enter your question (ex. 3 * 2): ")
calculator(ques)


