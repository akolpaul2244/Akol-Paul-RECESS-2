#Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
Student_Dict = {
    'name' : 'Akol Paul',
    'College': 'CoCIS',
    'Course' : 'BSSE',
    'Age': 23,
    'Yeear of Study': 'II',
    'Technology' : 'AI & ML'
}

print(Student_Dict)

#Accessing a specific element
print(Student_Dict['College'])

#Adding a value
Student_Dict['RegNo'] = '22/U/22453'
Student_Dict['Email'] = 'akolpaul2244@gmail.com'
print(Student_Dict)

#Exercise 1
#Modifying a value
Student_Dict['Age'] = 26
Student_Dict['Yeear of Study'] = "III"
print('\n')
print('..................This is a modified dictionary..................')
print(Student_Dict['Age'])
print(Student_Dict['Yeear of Study'])
print(Student_Dict)

# Exercise 2: Remove a key and value from student dictionary
del Student_Dict['Age']
print('\n')
print("Hey! i have removed age from the dictionary!")
print(Student_Dict)

#common methods in dictionaries
#get() // returns the value for the specified key if the key is in the dictionary
#if not it returns the default value
print('\n')
print('Hey! i want to access Technology')
print(Student_Dict.get('Technology'))

#update() // Updates the dictionary with the elements from another dictionary
#Exercise 3 use update method to change the value of course
Student_Dict.update({'course': 'BIST'})
print('\n')
print("Hello! i have updated the course name")
print(Student_Dict)

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary
if 'College' in Student_Dict:
    print('\n')
    print("The Student's College is: ", Student_Dict['College'])
else:
    print("The College doesn't exist in the dictionary")
    
# keys(), values() and the items() methods
print('\n')
print("Hey these are more methods")
print(Student_Dict.keys())
print('\n')
print(Student_Dict.values())
print('\n')
print(Student_Dict.items())

# Exercise 5 : Use the update method to change the course and add a new 
# key "WhatsApp_Number" to the dictionary
Student_Dict.update({'Course': 'BLIS'})
Student_Dict['WhatsApp_Number'] = '0782457648'
print('\n')
print('Hey! I have updated the course name and added my WhatsApp Number!')
print(Student_Dict)


#pop() // Removes the specified key and return the corresponding value
Technology = Student_Dict.pop('Technology')
print('\n')
print(Technology)
#print(Student_Dict.pop('Technology'))




