# Created with Pyto


import os

act_dir = os.getcwd()

print("Hello World! MK")
print(act_dir)


file = "test.txt"
with open(file, "w") as file_handle:
    for i in range(10):
        file_handle.write("Hannover")        

