from sys import argv

script, user_name = argv
response = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"Do you know me {user_name}?")
knows = input(response)

print(f"Where do you live {user_name}?")
lives = input(response)

print("What kind of computer do you have?")
computer = input(response)

print(f"""
Alright, so you said {knows} about knowing me.
You live in {lives}. I hope you enjoy living there.
And you have a {computer} computer. Nice.
""")
