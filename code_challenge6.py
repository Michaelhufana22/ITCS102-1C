#Get the factorial of the number 

number = eval(input("Enter a number : "))
factorial = 1
for me in range(number, 0, -1) :
	factorial *= me
print("The factorial of ",number,"is",factorial)