
from typing import Literal
#Inheritance and polymorphism
"""_summary
    Inheritance and method overriding
    polymorphism and method resolution order
    Abstract classes and interfaces
    """
    # Inheritance and method overriding
"""_summary
    --description
    Inheritance and method overriding allows a class(child class)to inherit attributes and methods from another class(parent class)
    Key concepts
    Base class (parent class): Class whose properties are inherited by another class.
    Derived class (child class): Class that inherits attributes and properties from another base class.


    """
#Example 1:Syntax create a class where a dod inherits from animal and overrides with the speak method
class Animal: # type: ignore
    def speak(self) -> str:
        return "Mwe Mwe Mwe Mwe"

class Dog(Animal): # type: ignore
    def speak(self) -> str:
        return 'Barks'

# Implementation
animal = Animal()
dog = Dog()
print(dog.speak())
    
# polymorphism
#polymorphism allows objects of different classes to be treated as objects of a common super class.
#Method resolution order (MRO) is order in which python looks for a method in a hierarchy classes.
#  #Example 2:How polymorphism works in python
class Animal:
    def speak(self):
        return "Crock"
class Dog(Animal):
    def speak(self) -> str: # type: ignore
        return "Barks"
class Cat(Animal):
    def speak(self) -> str: # type: ignore
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())
        
    make_animal_speak(Dog())
    make_animal_speak(Cat())
    
#Exercise 1:Create a simple application to manage different types of vehicles , Implement
#Derived class to demonstrate inheritance and polymorphism
"""summary
    Requirements
    1 baseclass to vehicles
    Attributes:make,model and year Methods:display_info()
    2,Derived classes
    car:inherit from vehicle
    attributes: number_of_doors
    overrides: display_info()
    Motorcycle:inherits from vehicle
    Attribute,type_of_bike(cruiser,sport,touring)
    #Exercise 2:
    create a function that accepts a list of vehicles and call their display_info()method to print details of each vehicle
    
"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.type_of_bike}")

# Exercise 2
def display_vehicles_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # For better readability

# Example usage:
car1 = Car("Toyota", "Camry", 2020, 4)
motorcycle1 = Motorcycle("Yamaha", "YZF-R3", 2021, "Sport")

vehicles = [car1, motorcycle1]
display_vehicles_info(vehicles)

#Reading and writing files in python
"""
    summary
    1. working with text files
    handling CSV files
    JSON and XML files processing
    """
    #1. working with text files ,open,read,write and close
    # note:python provides inbuilt functions to handle text files.
    #key concepts
"""
    summary
    description
    opening file:open() function (r,w,a,r+)
    reading file: read() function
    writing file:write() function
    close file:close() function
    """
    # example 3: write a file and read a file
    # writing to a text file
with open('jeff.txt','w') as file:
    file.write('iam jeff Geoff and i love python.\n')
    file.write('i used python for automation')
    
    # reading from a text file
with open('jeff.txt','r') as file:
    content=file.read()
    print(content)
    
    # handling CSV files
    """
    summary
    CSV  (comma separated values)file widely for data exchange.
    key concepts:
    reading CSV file:using 'CSV.reader()'
    writing CSV files:Using 'CSV.Writer'
    DictReader and DictWriter: the class read and write CSV files as dictionaries
    """
# example 4: reading CSV file
import csv
# writing to a CSV file
with open('jeff.csv','w',newline='') as csv_file:
    writer= csv.writer(csv_file)
    writer.writerow(['name','position','course'])
    writer.writerow(['Jeff Geoff','lecturer','BSE'])
    writer.writerow(['Paul','student','BSE'])
    writer.writerow(['Akol','student','BSE'])

# read from CSV file  
with open('jeff.csv','r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print (row)  
            #JSON and XML file processing
"""
JSON (javascript object notation) and XML (extensible markup language ) are formats used to structure data.

key concepts
loading JSON data:using json.load() for reading JSON file
dumping JSON DATA:Using json.dump() for writing JSON file
parsing JSON data: using json.loads() for handling JSON strings

"""
# example 6: write and read JSON File
import json
# writing to a JSON file

student_data={
    'name':'Paul',
    'course':'BSSE',
    'year':'year 3'
    
    
}
with open('student data.json','w') as json_file:
    json.dump(student_data,json_file)
    # reading the JSON file
with open('student data.json','r') as json_file:
    student_data=json.load(json_file)
    print(student_data)
    
    #Exercise 2: write and read the xml file
    import xml.etree.ElementTree as ET

def write_xml(file_name):
    # Creating the root element
    root = ET.Element("vehicles")

    # Creating a sub-element
    car = ET.SubElement(root, "car")
    ET.SubElement(car, "make").text = "Toyota"
    ET.SubElement(car, "model").text = "Corolla"
    ET.SubElement(car, "year").text = "2020"

    bike = ET.SubElement(root, "bike")
    ET.SubElement(bike, "make").text = "Yamaha"
    ET.SubElement(bike, "type").text = "Sport"
    ET.SubElement(bike, "year").text = "2019"

    truck = ET.SubElement(root, "truck")
    ET.SubElement(truck, "make").text = "Ford"
    ET.SubElement(truck, "capacity").text = "F-150"
    ET.SubElement(truck, "year").text = "2021"

    # Create a new XML file with the results
    tree = ET.ElementTree(root)
    tree.write(file_name)

def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for vehicle in root:
        print(f"Vehicle Type: {vehicle.tag}")
        for detail in vehicle:
            print(f"{detail.tag.capitalize()}: {detail.text}")
        print()

# Example usage
write_xml("vehicles.xml")
read_xml("vehicles.xml")
    
#Exercise 3: using abstraction calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)

rect = Rectangle(10, 5)
print("Area:", rect.area())  
print("Perimeter:", rect.perimeter())
