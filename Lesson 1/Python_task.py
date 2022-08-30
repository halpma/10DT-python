# O W  Holmes
#variables, output labels

# Decleration of variables
from unicodedata import numeric

# variables
name = "Oliver"
height = "5 feet and 10 inches"
adress = "19 Athens street, in the city of Wellington in New Zealand"
number = "020 408 18683"
hasAllergy = False 

# Full name
fullNameInitals = "O W Holmes"
fullName = "Oliver Wray Holmes"
firstName = "Oliver"
lastName = "Holmes"

# Phone number
countryCode = "64 020 408 18683"

# Adress
streetNumber = "19"
streetName = "Athens Street"
suburb = "Mirimar"
town = "Wellington"

# Height
heightFeet = "five"
hightInches = "10"

# Output  of variables to screen
print(type(name))
print(type(height))
print(type(adress))
print(type(number))
print(type(hasAllergy))

# Output  of variables with labels to screen
print("My first name is",name,)
print("my height is",height,"And I am still growing quite quickly")
print("I move quite alot but at the moment I live at",adress)
print("If you want to contact me my phone number is",number)
print("And if you think that I have any allergys that information is",hasAllergy)