"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 6: Files
14/4/2017
"""

def my_function(file1, file2):
    if not file1.endswith(".py"):
        return -1

    with open(file2, 'w') as f1:
        for line in open(file1, "r"):
            if "#" in line:
                comment = line[line.index("#"):]
                f1.write(comment)
    

my_function("test.py","new.py")
       
        
                
                    
                    
    
	
