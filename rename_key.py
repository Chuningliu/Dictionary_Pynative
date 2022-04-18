# Write a program to rename a key city to a location in the following dictionary.
a= {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
} 
a["location"]=a["city"]
del a["city"]
print(a)


