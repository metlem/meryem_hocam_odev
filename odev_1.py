#Factorial    

#Step 1 : Solution with recursion func
def factorial_1(n : int):
	if n < 0: 
		return "Please enter a positive number"
	elif n == 1 or n == 0:
		return 1
	else:
		return n*factorial_1(n-1)


#Step 2 : Solution with list data type
def factorial_2(n : int):
	numbers = []
	for number in range(1, n+1):
		numbers.append(number)
	
	fact = 1
	for i in numbers:
		fact = fact*i
	return fact


#-------------------------------------------------------------------------------

#Fibonocci

#Step 1 : Solution with recursion func
def fibonocci_1(n):
	if n == 1 or n ==2:
		return 1		
	elif n <= 0:
		return "Please write more than 1."
	else:
		return fibonocci_1(n-1) + fibonocci_1(n-2)

#Step 4:
def fibonocci_2(n):
	first_number , second_number = 1, 1
	for i in range(n-1):
		first_number , second_number = second_number, first_number + second_number
	return first_number


try:
	inp_1 = int(input("Step 1 -> factorial( ? ) -> ? = "))
	print(inp_1,"! = ", factorial_1(inp_1))

	inp_2 = int(input("Step 2 -> factorial( ? ) -> ? = "))
	print(inp_2,"! = ", factorial_1(inp_2))

	inp_3 = int(input("Step 3 -> fib( ? ) -> ? = "))
	print("fib(",inp_3,") = ", fibonocci_1(inp_3))

	inp_4 = int(input("Step 4 -> fib( ? ) -> ? = "))
	print("fib(",inp_4,") = ", fibonocci_1(inp_4))
except :
	print("Please write number!!! ")

