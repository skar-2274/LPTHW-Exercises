def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some maths with just functions!")

age = add(15, 5)
height = subtract(180, 16)
weight = multiply(6,9)
ratio_of_exercises_completed = divide(21,52)

print(f"Age: {age} years old, Height: {height} cm, Weight: {weight} kg and the ratio of this book read: {ratio_of_exercises_completed}")

print("Here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(ratio_of_exercises_completed, 2))))

print("That becomes: ", what," Can you do it by hand?")
