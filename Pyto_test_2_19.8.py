# Created with Pyto


import os

act_dir = os.getcwd()

print("Hello World! MK")
print(act_dir)


file = "test.txt"
with open(file, "w") as file_handle:
    for i in range(10):
        file_handle.write("Hannover\n")
        
# file_handle.close()

file = "pyto_test.txt"

with open(file, "r") as file_handle:
    s = file_handle.readlines()
    
    
print(s)
        
