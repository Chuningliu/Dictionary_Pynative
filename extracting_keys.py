# Write a Python program to create a new dictionary by extracting 
# the mentioned keys from the below dictionary.


a = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
c= ["name", "city"] 
b= {i:a[i] for i in c}
print(b)

