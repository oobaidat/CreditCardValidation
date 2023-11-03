import random

# Counter for how many credit card numbers to generate and check
counter = 5
while counter > 0:
    # Variable to store the randomly added digits
    randomNumber = ""
    
    # Randomly chooses a number between 12 and 17
    randomLength = random.randint(12,17)
    # Randomly joins digits from a pool of digits to the string 
    # till the string's length is equal to the randomly chosen length
    for length in range(randomLength):
        randomNumber += (random.choice("0123456789"))

    # Check if the number inputted is potentially a valid credit card number
    if randomNumber.startswith(("4", "5", "37", "6")) and 13 <= len(randomNumber) <= 16:
        # Variable to store the number to be used as a check
        checkNumber = 0
        # Loop through the number backwards and double every second digit
        # (The end value of the range is -1 as it is exclusive)
        for position in range(len(randomNumber)-2, -1, -2):
            doubledDigit = int(randomNumber[position])*2
            # Add the digits of the doubled digit to the check number
            checkNumber += doubledDigit%10
            checkNumber += doubledDigit//10
                
        # Loop through the number backwards and add every second digit
        # to the check number starting from the right most digit
        for position in range(len(randomNumber)-1, -1, -2):
            checkNumber += int(randomNumber[position])

        # If the check number is a multiple of 10 it is valid
        if checkNumber%10 == 0:
            print("Randomly generated credit card number: " + randomNumber + "\nIs valid")
        else:
            print("Randomly generated credit card number: " + randomNumber + "\nIs invalid")

    # The number failed the first check
    else:
        print("Randomly generated credit card number: " + randomNumber + "\nIs invalid")
    
    counter -= 1