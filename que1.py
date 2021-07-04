import hashlib
str="project"
output=hashlib.md5(str.encode())
print("The value of hashlib =")
print(output.hexdigest())