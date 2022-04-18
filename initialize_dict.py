# Initialize dictionary with default value:
def items(name,defaults):
    a= dict.fromkeys(name, defaults)
    print(a)
name = ['Ning', 'Matt']
defaults = {"designation": 'Developer', "salary": 8000}
items(name,defaults)


