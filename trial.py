
from unittest import result

#This prompts a student to enter his/her details
name = input('What is your name?\n')
RegNo = input('Enter your Registration number\n')
StdNo = input("Enter your Student's number\n")
campus = input('Which campus do you study?\n')
college = input('What is your college?\n')
course = input('which course do you do?\n')
year = input('What is your year of study?\n')
favorite_color = input('What is your favorite color\n')
#print students information
print("...............Student's info...................")
print("Name:"+ " " +name)
print("Registration number:"+ " " +RegNo)
print("Student's number:"+ " " +StdNo)
print("Campus:"+ " " +campus)
print("College:"+ " " +college)
print("Course:"+ " " +course)
print("Year of study:"+ " " +year)
# Print the user's name and favorite color using f-strings for clarity
print("My favorite color is"+" "+favorite_color)