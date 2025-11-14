print("\n========== DATA ENTRY ==========\n") # Program Title

n = int(input("Enter a number: ")) # Request an integer from the user

if n < 2: # Check if the number is less than 2
    print(n, "is NOT prime (prime numbers are 2 or greater).") # Inform it's not prime
else: # If the number is 2 or greater, proceed to check
    i = 2 # Initialize the divisor at 2
    is_prime = True # Assume the number is prime until proven otherwise

    while i < n: # Loop through all numbers from 2 up to n-1
        if n % i == 0: # Check if n is divisible by i
            is_prime = False # If it is divisible, it's not prime
            break # Exit the loop immediately
        i += 1 # Increment the divisor

    if is_prime: # If the loop finished without finding a divisor
        print(n, "IS prime.") # Inform the user it is prime
    else: # If the loop was broken
        print(n, "is NOT prime. It is divisible by", i) # Inform it's not prime and show the divisor