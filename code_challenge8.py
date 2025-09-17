print("MULTIPLICATION TABLE MAKER")
user = eval(input("Enter a number : "))
print("\nMultiplication for number",user,':')
for me in range(1,11) :
	print(user,'x',me,'=',user*me)