#Caesar Cipher Program
import string

#Initializing Empty Array
letters_lower = []
letters_upper = []

#Filling Array with Alphabete
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)

start = input("Encrypt or Decrypt?:\n")
if start == "Encrypt":

    #Asking User For Message to Encrypt
    phrase = input("Phrase To Be Encrypted: \n")

    #asking User For Shift Number
    shift = input("Input shift value As A Positive Number: \n")

    #Checking To Make Sure User Input For Shift Is A Number
    if (shift.isnumeric() == False):
        #If User Input Is Not A Number Keep Asking Until A Numeric Input Is Given
        while (shift.isnumeric() == False):
            shift = input("Please Enter A Positive Numeric Shift Value: \n")

    #Changing the variable from a string to an integer
    shift = int(shift)

    #Getting Rid Of Any Spaces At The Beginning And End Of The Message
    phrase.strip()
    ans = ""

    #Looping Over Given Message
    for x in phrase:
        #If the Given Index In phrase Is A Space, Then Add It To ans, Then Move On To The Next Index
        if x == " ":
            ans = ans + x
            continue
        #If The Current Letter Is Uppercase, Find the New Shifted Letter In The Array Of Uppercase Letters
        elif x.isupper() == True:
            ans = ans + letters_upper[letters_upper.index(x) + shift]
        #If The Current Letter Is Lowercase, Find the New Shifted Letter In The Array Of Lowercase Letters
        elif x.islower() == True:
            ans = ans + letters_lower[letters_lower.index(x) + shift]
        
    #Returning Encrypted Message
    print("Encrypted Message: " + ans)
else:
    #Asking User For Message to Decrypt
    phrase = input("Phrase To Be Decrypted: \n")

    #Asking User For Shift Number
    shift = input("Input Original Shift Value: \n")

    #Checking To Make Sure User Input For Shift Is A Number
    if (shift.isnumeric() == False):
        #If User Input Is Not A Number Keep Asking Until A Numeric Input Is Given
        while (shift.isnumeric() == False):
            shift = input("Please Enter A Positive Numeric Shift Value: \n")

    #Changing the variable from a string to an integer
    shift = int(shift)

    #Getting Rid Of Any Spaces At The Beginning And End Of The Message
    phrase.strip()
    ans = ""

    #Looping Over Given Message
    for x in phrase:
        #If the Given Index In phrase Is A Space, Then Add It To ans, Then Move On To The Next Index
        if x == " ":
            ans = ans + x
            continue
        #If The Current Letter Is Uppercase, Find the New Shifted Letter In The Array Of Uppercase Letters
        elif x.isupper() == True:
            ans = ans + letters_upper[letters_upper.index(x) - shift]
        #If The Current Letter Is Lowercase, Find the New Shifted Letter In The Array Of Lowercase Letters
        elif x.islower() == True:
            ans = ans + letters_lower[letters_lower.index(x) - shift]
        
    #Returning Decrypted Message
    print("Decrypted Message: " + ans)





