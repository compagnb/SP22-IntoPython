# Variables
# cannot start with a capitol letters
# cannot use  space or special characters
# Instead use camelcase and uderscores

#Hi my name is Hame, and I am age years old.
#In 10 years I will be age+10 year"

name = input("Please enter your name.")
age = input("Please enter your age.")
ageInTenYears = int(age) + 10

statement = "Hi my name is " + str(name) + " and I am" + age + " years old. In 10 years I will be " + str(ageInTenYears) + "years old."
print(statement)
