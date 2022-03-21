# Hi my name is Name and I am age years old.
# In 10 years, I will be age+10
# cannot use capials,spaces or special characters

name = input( "What is your name?")
age = input ( "How old are you")
ageInTenYears =  int(age) + 10

statement = "Hi my name is" + name +  "and I am" + age + " years old. In 10 years, I will be " + str(ageInTenYears) + "years old"
print(statement)
