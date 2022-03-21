# Variables
# cannot start with capitol letters!
# cannot use spaces or special chracters
# instead of spaces use camelCase or under_scores

# Hi my name is Name, and I am age years old.
# In 10 years I will be age+10 years old.

name = input("What is your name?")
age = input("How old are you?")
ageInTenYears = str(int(age) + 10)

statement = "Hi my name is " + name + ", and I am " + age + " years old. In 10 years I will be " + ageInTenYears + " years old."
print(statement)
