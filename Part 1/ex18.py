#this works like the argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#the args is pointless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#zero arguments
def print_none():
    print("I got nothing.")

print_two("Surajit","Kar")
print_two_again("Surajit","Kar")
print_one("First!")
print_none()
