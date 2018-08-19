i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def new_numbers(max, increments):
    i = 0
    number_list = []
    while i < max:
        print(f"At the top i is {i}")
        number_list.append(i)

        i += increments

    print("This number list: ")

def for_new_numbers(max, increments):
    for i in range(0, max, increments):
        print(f"The list is {i}")

new_numbers(10,2)
for_new_numbers(30,3)
