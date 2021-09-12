import hashlib
str=import ("Enter the input")
output=hashlib.md5(str.encode())
print("The value of hashlib =")
print(output.hexdigest())
