import re 
import os
r = re.compile(".*stat$")

print(list(filter(r.match, os.__dict__.keys())))

# print( os.__dict__.keys())


print("hello how r u ".split(" "))