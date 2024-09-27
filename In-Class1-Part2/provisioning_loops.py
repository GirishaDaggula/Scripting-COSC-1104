"""
Author1: Girisha Daggula(100974333)
Author2: Lalitha Sri Chennapragada(100979071)
Date: 27/09/2024
Description: The following program imitates a cloud resource provisioning system extension to the previous code. 
The user provides username under user_input.
The number of CPU cores and the amount of memory required in GB will be provided by the user.
The below program will determine whether there are sufficient resources available or not. 
Displays the result either as remaining resources available or as provisioning failed and provisioning successfully.
Displays the result in table format and shows the pending requests as well.
"""
#Declarations
Total_CPU_Cores = 12
Total_Memory_GB = 32.0
#Empty lists()
allocated_resources = list()
pending_requests = list()
Remaining_CPU_Cores = Total_CPU_Cores
Remaining_Memory_GB = Total_Memory_GB
#While loop 
while True:
    user_input = input("Enter the username: ")
    Selected_CPU_Cores = int(input("Enter the number of CPU Cores required: "))
    Selected_Memory_GB = float(input("Enter the amount of memory required in GB: "))
    if Selected_CPU_Cores <= Remaining_CPU_Cores and Selected_Memory_GB <= Remaining_Memory_GB:
        print("Resources Provisioned Successfully")
        allocated_resources.append([user_input, Selected_CPU_Cores, Selected_Memory_GB])
        Remaining_CPU_Cores -= Selected_CPU_Cores
        Remaining_Memory_GB -= Selected_Memory_GB
    else:
        print("Resources request exceed capacity. provisioning failed")
        pending_requests.append([user_input, Selected_CPU_Cores, Selected_Memory_GB])
    continue_input = input("Do you want to allocate more resources? (yes/no): ")
    if continue_input.lower() != 'yes':
     break
#To  view allocated resources
print("\nallocated_resources:")
print(f"{'username':<20} {'Selected_CPU_Cores':<12}{'Selected_Memory_GB':<32}")
print(f"-" * 60)
for allocation in allocated_resources:
    user_input, Selected_CPU_Cores, Selected_Memory_GB = allocation
    print(f"{user_input:<20}{Selected_CPU_Cores:<12}{Selected_Memory_GB:<32}")
 #To view pending requests  
print("\n pending requests:")
print(f"{'user_input':<20}{'Selected_CPU_Cores':<12}{'Selected_Memory_GB':<32}")  
print(f"-" * 60)
for request in pending_requests:
    user_input, Selected_CPU_Cores, Selected_Memory_GB = request
    print(f"{user_input:<20}{Selected_CPU_Cores:<12}{Selected_Memory_GB:<32}")
 #To display the remaining resources   
print("\nRemaining Resources:")
print(f"Remaining CPU Cores: {Remaining_CPU_Cores}")
print(f"Remaining Memory GB: {Remaining_Memory_GB}")   


     
        
        
        
        
        

        
