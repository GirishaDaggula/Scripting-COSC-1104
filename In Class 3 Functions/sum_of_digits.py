"""
Author1: Girisha Daggula(100974333)
Author2: Lalitha Sri Chennapragada(100979071)
Date: 04/10/2024
Description: The following program will test the sum of digits using functions concept.
Displays the output as the numbers given below. 

"""

# defining function
def is_sum_of_digits(number: int):      # the number parameter having the data type called int
    if (number < 0):                     # Stating the condition if the number is less than zero, returns invalid
        print("Invalid input. Enter a valid number")
        return None                      
        
    total = 0  # total should be zero at initial stage, only then when it adds up the number given as below and displays the correct output.
    while(number > 0):                   
        total += number %10                # adding the last digit to total
        number //= 10                   # performing the integer division using assignment operator
    return total

if __name__ == "__main__":               # Demonstarting the functionality of function and providing the numbers to display output
    
    print(is_sum_of_digits(535))
    print(is_sum_of_digits(289))
    print(is_sum_of_digits(621))
    print(is_sum_of_digits(476))
    print(is_sum_of_digits(227))
    print(is_sum_of_digits(-325))
    