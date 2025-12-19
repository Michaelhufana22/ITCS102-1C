import time

print("WELCOME TO MENU COMPILER")
print("---------------------------------------")

name = input("Please insert your name first --> ")
print(f"Hi {name}, Welcome to the menu compiler!")

while True:
    print("\nChoose one from the menu:")
    print("1. Print in Python")
    print("2. Variables")
    print("3. Operators and its use")
    print("4. Conditional Statement")
    print("5. Loop")
    print("6. List")
    print("7. Functions")
    print("8. Exit")

    choice = input("Enter your preferred choice: ")

    if choice == '1':
        while True:
            time.sleep(2)
            print("---------------------------------------")
            print("\nPRINT MENU")
            print("1. Definition")
            print("2. Example print")
            print("3. Back to main menu")

            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(3)
                print("\nDefinition:\n")
                print("The print() function in Python can handle various data types, including strings, integers, and floats. To output a string, simply pass it as an argument to the print function.")
            
            elif sub_choice == '2':
                time.sleep(3)
                print("\nExample:")
                print("print('Hello world')")
                print("\nOutput:")
                print("Hello world")
                print("---------------------------------------")
            
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '2':
        while True:
            time.sleep(2)
            print("\nYou selected Variables")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("---------------------------------------")
                print("\nDefinition:\n")
                print("A variable is a named value that can be stored and used later.")
                print("\n---------------------------------------")
                
            elif sub_choice == '2':
                time.sleep(3)
                print("---------------------------------------")
                print("\nExample: ")
                print("word = Python " )
                print("print(word)")

                print("\nOutput:")
                print("Python")
                print("\n---------------------------------------")
                
            elif sub_choice == '3':
                print("Going back to main menu\n")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '3':
        while True:
            time.sleep(2)
            print("---------------------------------------")
            print("\nYou selected Operators")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            print("\n---------------------------------------")

            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("\nDefinition:\n")
                print("Operators are symbols that perform operations on variables and values.")
                
                print("---------------------------------------")
            
            elif sub_choice == '2':
                time.sleep(3)
                print("---------------------------------------")
                print("Examples: ")
                print("a = 33")
                print("The value of a is a")
                
                print("a += 6")
                print("a -= 20")
                print("a *= 14")
                print("a %= 19")
                
                print("The value of a is " 'a')
                
                print("Output:\na = 33\nThe value of a is 33\na += 6 | New value of a: 39\nna -= 20 | New value of a: 19\na *= 14 | New value of a: 266\na %= 19 | New value of a: 0\nThe final value of a is 0")
                                
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '4':
        while True:
            time.sleep(2)
            print("\n---------------------------------------")
            print("\nYou selected Conditional Statements")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            
            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("---------------------------------------")
                print("\nDefinition:\n")
                print("Conditional statements allow you to execute a block of code if a certain condition is true. In Python, the if-elif-else structure is used.")
            elif sub_choice == '2':
                time.sleep(3)
                print("\nExample:")
                print("age = 18")
                print("if age >= 18:")
                print("print('You are an adult')")
                
                print("else:\n\tprint('You are young')")
                print("\nOutput:")
                print("You are an adult")
            
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '5':
        while True:
            time.sleep(2)
            print("\nYou selected Loop")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("---------------------------------------")
                print("\nDefinition:\n")
                print("Loops are used to execute the code easily.In Python, the 'for' loop and 'while' loop are commonly used.")
                print("\n---------------------------------------")
            elif sub_choice == '2':
                time.sleep(3)
                print("\nExample with a 'for' loop:")
                print("print for i in range(5,0,-1):\n\tprint(i)")
                  
                
                print("\nExample with a 'while' loop:")
                print("i = 5\nwhile i > 0:\n\tprint(i)\n\ti -= 1")
                
                print("\nOutput:")
                print("5\n4\n3\n2\n1\n")  # For loop output
                print("5\n4\n3\n2\n1\n")  # While loop output
                print("\n---------------------------------------")
            
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '6':
        while True:
            time.sleep(2)
            print("\n---------------------------------------")
            print("\nYou selected Lists")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("\n---------------------------------------")
                print("\nDefinition:\n")
                print("A list is a collection of items in a particular order. Lists are mutable, meaning you can change their content.")
            
            elif sub_choice == '2':
                time.sleep(3)
                print("\nExample:")
                print("my_list = [bagoong,mangga, mansanas, santol, saging]")
                print("print(my_list)")
                
                print("\nOutput:")
                print("[ bagoong,mangga, mansanas, santol, saging ]")
                
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '7':
        while True:
            time.sleep(2)
            print("---------------------------------------")
            print("\nYou selected Functions")
            print("1. Definition")
            print("2. Examples")
            print("3. Back to main menu")
            print("\n---------------------------------------")
            sub_choice = input("Choose: ")

            if sub_choice == '1':
                print("Loading please wait.....")
                time.sleep(2)
                print("---------------------------------------")
                print("\nDefinition:\n")
                print("A function only runs when it is called. Functions can take parameters and return a value.")
            
            elif sub_choice == '2':
                time.sleep(3)
                print("\n---------------------------------------")
                print("\nExample:")
                
                print("def greet(name):")
                print(" return f'hello,{name} ")
                
                print("result = greet('name')")
                print("print (result)")

                print("\nOutput:")
                print("Hello, Hufana!")
        
            elif sub_choice == '3':
                print("Going back to main menu")    
                break

            else:
                print("Invalid choice, please choose again..")

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please choose again..")