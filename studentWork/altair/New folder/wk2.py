#Variables
#cannot use capital letters!
#cannot use spaces or special characters
# instead use camelcase or under_score

#Hi my name is Name, and I am age years old.
# In the 10 years I will be age+10 years"

name= input("Enter you name.")
age = input("Enter your age.")
ageInTenYears = int(age) + 10

statement = "Hi my name is "+ name +", and I am" + age + " years old. In 10 years I will be:" +  str(ageInTenYears) + "years old."
print (statement)
