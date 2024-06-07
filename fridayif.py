age = int(input("Enter age\n"))

if(age <= 13):
    print("Hey! your discount is 1000")
elif age > 13 and age <= 18:
    print("Hey, your discount is 500")
elif age > 18 and age <= 50:
    print("Hey, you are an adult but not a senior citizen,\n")
    print("You don't have discount \n")
    print("Your pay is 2000.")
else:
    print("Hey you are a Senior citizen, pay 5000")   