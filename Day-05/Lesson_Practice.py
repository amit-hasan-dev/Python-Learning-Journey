#Day 05: Operators.

#01. Arithmetic Operators.

#arithmetic operators perform mathematical calculations.
# (+) = Addition - 6+4 = 10
# (-) = Subtraction - 6-4 = 2
# (*) = Multiplication - 6*4 = 24
# (/) = Division - 6/3 = 2
# (//) = Floor Division - 5//3 = 1
# (%) = Remainder - 5%3 = 2
# (**) = Power - 5**3 = 125
first_number = int("6")
second_number = int("4")
third_number = int("5")
forth_number = int("3")
print("Example: ")
print(first_number + second_number)
print(first_number - second_number)
print(first_number * second_number)
print(first_number / forth_number)
print(third_number // forth_number)
print(third_number % forth_number)
print(third_number ** forth_number)
print()
#Assignment Shortcuts
x = 6
x += 4
print(x)
print()
#similar shortcuts include:
x -= 2
print(x)
x *= 5
print(x)
x /= 3
print(x)
x //= 2
print(x)
x %= 3
print(x)
x **= 2
print(x)
print()

#02. Operator Precedence.

#operator precedence decides which operation python performs first. 
#from highest to lowest: 
#1. Parentheses : ( )
#2. Exponentiation : *
#3. Unary Operators : +x, x
#4. Multiplication & Division : /, //, %
#5. Addition & Subtraction : +, -
#6. Logical : not
#7. Logical : and
#8. Logical : or
result = 5+4*7
print(result) #33
print()
#Here multiplication is performed before addition.#Use "Parentheses" to change the order:
result = (5+4)*7
print(result) #63
print()
#Operators at the same level are generally evaluated from left to right.
result = (20/5*2)
print(result) #8.0
print()
#Exponentiation is evaluated from right to left:
result = (2**3**2)
print(result) #512
print()
#Use parentheses whenever they make and expression clearer.

#03. Comparison Operators.

#Comparison Operators compare two values and return "True" or "False".
# 1. > - Greater than
# 2. < - Less than
# 3. >= - Greater than or Equal to
# 4. <= - Less than or Equal to
# 5. == - Equal to
# 6. != - Not equal to  
first = '5'
second = '1'
print(first > second) #5>1 true
print(first < second) #5<1 false
print(first >= second) #5>=1 true
print(first <= first) #5<=5 true
print(first == first) #5==5 true
print(first != first) #5!=5 false
print()
# "=" assigns a value, while "==" compares two values:
age = 18 #(Assignment)
print(age == 18) #(Comparison)
print()

#04. Logical Operators.

#Logical operators combine or reverse conditions.

# ("or") returns "true" when at least one condition is true.
print(5 > 2) or (2 > 5) #true
print()

#("and") returns "true" only when both conditions are true.
print((5 > 2) and (2 < 5)) #true
print((5 > 2) and (2 > 5)) #false
print()

#("not") Reverses a boolean result. 
print(not(5 > 2)) #false
print(not(10 == 10)) #false
print(not(3 > 5)) #true
print()

#05. Conditional Statements.

#Conditional Statements run code based on whether a condition is "True" or "False".

#("if")
age = 20
if age >= 20:
	print("You're Selected!")
	print("You're Eligible!")
	print()
#a colon(":") is required after the condition. Code inside the block is intended using four spaces.

#("if - else")
age = 16
if age >= 18:
	print("You're selected!'")
	print("You're choosen!")
else:
	print("You're not eligible!")
	print()
	
#("if - elif - else")
#use ("elif") when there are multiple conditions.
age = int(input("Enter your age: "))
if age > 90:
	print("You're over the allowed age.")
elif age >= 18:
	print("You're allowed to drive.")
else:
	print("You cannot drive.")
	print()
#python check conditions from top to bottom and runs only the first matchinh block.

#Combining Conditions:
age = int(input("Enter your age: "))
if age >= 18 and age <= 90:
	print("You're within the allowed age range.")
else:
	print("You're outside the allowed age range.")
	print()
	
#Python also supports chained comparisons.
if 18 <= age <= 90:
	print("You can drive!")
	
print("==== End of Day 03's Lesson ====")