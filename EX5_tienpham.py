"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 5: Loops
14/4/2017
"""
from numbers import Number 

Test1 = [1,2,3,4,"5"]
Test2 = [1,2,3,4,5]
Test3 = [1,2,3,4,0,5]

def my_function(input_list):

        for value in input_list:
                if not isinstance(value,Number):
                        return 0

        listSum = 0
        index = 0
        while index < len(input_list):
                if input_list[index] != 0:
                        listSum += input_list[index]
                else:
                        break
                index += 1

        return listSum

print(my_function(Test1)) 
print(my_function(Test2))
print(my_function(Test3))
        
                
                    
                    
    
	
