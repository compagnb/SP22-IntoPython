# Variables
# cannot start with capital letters!
# cannot use spaces or special characters
# instead of spaces use camelCase or under_scores
# Hi my name is Name, and I am age years old.
# In 10 years I will be age + 10 years.

name = input("Enter your name.")
age = input("Enter your age.")
ageInTenYears = str(int(age) + 10)

statement = "Hi my name is " + name + " and I am " + age + " years old. In 10 years I will be " + ageInTenYears + " years old."
print(statement)
