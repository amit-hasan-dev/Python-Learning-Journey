a = float(input("Enter your number: "))
b = float(input("Enter your number: "))
opp = input("Enter your operator (+, -, *, %, **): ")

if opp == "+" :
	print("Your answer is: ", a + b)
elif opp == "-" :
	print("Your answer is: ", a - b)
elif opp == "*" :
	print("Your answer is: ", a * b)
elif opp == "%" :
	print("Your answer is: ", a % b)
elif opp == "**" :
	print("Your answer is: ", a ** b)
else:
	print("Syntax Error!")