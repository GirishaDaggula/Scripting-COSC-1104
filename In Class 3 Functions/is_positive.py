"""
Author1: Girisha Daggula(100974333)
Author2: Lalitha Sri Chennapragada(100979071)
Date: 04/10/2024
Description: The following program will test the numbers are positive or negative using functions concept.
Displays the output as True or False as given below. 

"""
# defining function
def is_positive(number: float): #the number parameter having data type called float which is used for decimal numbers
    if (number > 0):    # Stating the condition that the number should be greater than zero and return the result as true or false
        return True
    else:
        return False
     
     
if __name__ == "__main__":     # Demonstarting the functionality of function and providing the numbers to display output
    
    print(is_positive(3.5))
    print(is_positive(-2.3))
    print(is_positive(4.8))
    print(is_positive(10.0))
    print(is_positive(-1.0))
    
    