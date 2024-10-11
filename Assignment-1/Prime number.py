'''
Author : Daaggula Girisha
Date : 11/10/2024
Description : The following program is about to check whether the given number is prime or not.
Displays the result as the prime number befor and after.
Shows th factors of given user input.
'''

# To check whether entered number is a prime number or not
def is_prime_number(num):      #defining a function
    if num < 0:
        print("Enter a Valid Number")
        return False
    for i in range(2, num):           # for loop
        if(num % i == 0):
            return False
    return True
        
        
# To get the number before a prime number
def previous_prime (num):
    num -=1       # checking the numbers from given number
    while num >1:
        if is_prime_number(num):
         return num
        num -=1  
    return None 

# To get the number after a prime number
def next_prime (num):
    num +=1
    while True:
        if is_prime_number(num):
            return num
        num +=1
    return None

# function for finding factors for non-prime numbers
def get_factors(n):
    factors = [] 
    for i in range(1, n+1):
        if (n % i == 0):
            factors.append(i)     # if i divides n appending i to list
    return factors
     
def main():
    while True:
        user_input = input("Please enter the random number to check: ")

        # checking if the input value is digit and converting to integer
        if user_input.isdigit():
            num = int(user_input)

            # checking the number is positive or not
            if num > 0:
                break
            else:
                print("This is not a positive whole number. Please try again: ")
        else:
            print("Invalid input. Please enter a positive whole number. Try again")


# if the number is 1
    if num == 1:
        print("1 is not a prime number")
        print("There are no prime numbers before 1")
        print("Prime number after 1 is 2")
        return

# finding the previous prime number
    prev_prime = previous_prime(num)
    if prev_prime:
        print(f"The prime number before {num} is {prev_prime}")
    else:
        print(f"There is no prime number before {num}")

    
    # checking the number is prime or not
    if is_prime_number(num):
        print(f"{num} is a prime number")         
    else:                                    # getting the factors if number is not a prime    
        print(f"{num} is not a prime number")
        print(f"The factors of {num} are {get_factors(num)}")



    # finding the next prime number
    next_pr = next_prime(num)
    print(f"The prime number after {num} is {next_pr}")




# main function for script execution
if __name__ == "__main__":
    main()

