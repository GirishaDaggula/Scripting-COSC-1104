"""
Author1: Girisha Daggula(100974333)
Author2: Lalitha Sri Chennapragada(100979071)
Date: 04/10/2024
Description: The following program will test the power of two using functions concept.
Displays the output as True or False as given below. 

"""

# defining function
def is_power_of_two(number: int):    #the number parameter having data type called int    
    if(number <= 0):            # Stating the condition that  if the number less than zero, return the result as false
        return False
    x = 1
    while x < number:   #loop terminates if x is greater than number
        x *= 2           # the given numbers are multiplied twice
    return  x == number    # if the number satisfies the condition, it multiplies by 2 and returns true

if __name__ == "__main__":        # Demonstarting the functionality of function and providing the numbers to display output
    
    print(is_power_of_two(16)) 
    print(is_power_of_two(-32))  
    print(is_power_of_two(1))   
    print(is_power_of_two(0))   
    print(is_power_of_two(2))
  
        
    
    
    