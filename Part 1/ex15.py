#sys is a package
from sys import argv
#argv is defined
script, filename = argv
#file is opened
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read()) #file is read

print("Type the filename again:")
file_again = input("> ") #user input filename again

txt_again = open(file_again) #file is reopened
print(txt_again.read()) #file is re-read
txt.close() #file is closed
txt_again.close() #file is closed
