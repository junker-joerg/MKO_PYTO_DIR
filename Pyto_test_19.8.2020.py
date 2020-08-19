# Python Test - auf Github gleich eingecheckt
# !Todo: github aufräumen
# kann man snippits verarbeiten? zB aus carnets?


from __future__ import print_function, division

import numpy as np

'''
with np.printoptions(threshold=5, edgeitems=4):
    print(np.random.random(10))
'''    
  
  
file_contents = ""
with open("pyto_test.txt", "r") as file_handle:# Permission error - nur local
    for line in file_handle.readlines():
        file_contents += line.replace("-", "_")  
        
        