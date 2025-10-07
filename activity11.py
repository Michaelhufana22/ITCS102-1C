temp = eval(input("Enter Temperature outside:"))

if temp >= 1 and temp<= 20:	
	print("The temperatur is considered as Extreme cold")
elif temp >= 21 and temp<= 30:
	print("The temperatur is considered as cold")
elif temp >= 31 and temp<= 37:
	print("The temperatur is considered as lukewarm")
elif temp >= 38 and temp<= 45:
	print("The temperatur is considered as hot")
elif temp >= 45 and temp<= 50:
	print("The temperatur is considered as boiling hot")
elif temp >= 51 or temp <= 52 :
	print("The temperature is considered as dangerous temperature")
else:
	print("Invalid Temperature")
