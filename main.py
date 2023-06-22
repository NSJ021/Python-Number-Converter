# Number Coverter Challenge, by and for Nathan Jones

# Decimal to Binary function
def dec_to_bin(user_number):
    if user_number >= 1:
        #function call
        dec_to_bin(user_number // 2)    #floor divison of the users number
    print(user_number % 2, end = '')    #users number to a base 2, end = '' put all values on same line?


# convert to binary via bin() method
def dtb_basic(n):
    return bin(n).replace("0b", "")    #bin() method value to binary

# Binary to Decimal function
def bin_to_dec(user_number):
    return int(user_number, 2) # int() function takes a value and then a base, e.g binary is to base 2


# convert to hex via hex() method
def dth_basic(h):
    return hex(h)

#Decimal to Hexadecimal function
def dec_to_hex(user_number):
    if user_number <= 0:    #if user number is 0 or above
        return ''
    remainder = user_number % 16    # declaring remainder variable as modulo 16 of users input
    return dec_to_hex(user_number // 16) + hex_conversion_table[remainder]
    # returning the function with user number floor division 
    # whilst adding the corresponding value from the coversion table
    

# Hex conversion table
hex_conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
#Main code block if statement
if __name__ == '__main__':
    #getting user input
    print("Number Coverter\n")
    print("---------------------------------------------------------- \n")
    print("Choose Decimal: for Decimal -> Binary\n")
    print("------------------------------------------------ \n")
    print("Choose Binary: for Binary -> Decimal\n")
    print("------------------------------------------------ \n")
    print("Choose Hexaecimal: for Decimal -> Hexadecimal\n")
    print("------------------------------------------------ \n")
    user_choice = input("Please choose a number type, either Decimal, Binary, Hexadecimal: \n")


#If User chooses decimal program will covert it into binary
if user_choice == "Decimal" or user_choice == "decimal":
    #getting user input
    user_number = int(input("Enter a number to convert to binary: \n"))
    #calling dec to bin function
    
    print(f"Your binary number is: {(str(dtb_basic(user_number)))}")
    dec_to_bin(user_number)
    #print(str(dtb_basic(user_number)))
    

#If User chooses binary program will covert it into decimal
elif user_choice == "Binary" or user_choice == "binary":

        user_number = input("Enter a binary number to convert to decimal: \n")
        print(f"Your decimal number is: {bin_to_dec(user_number)}")
        

#If User chooses hexadecimal program will covert it into decimal
elif user_choice == "Hexadecimal" or user_choice == "hexadecimal":
        user_number = int(input("Enter a number to convert to hexadecimal: \n"))
        #print(type(user_number))
        print("Your decimal number is: " + hex(user_number))
        print(str(dec_to_hex(user_number)))
else:
    print("Your choice was not valid")
