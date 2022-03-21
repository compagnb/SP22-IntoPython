## Commands we used in python's shell:

### Print Hello
`print("hello world")`

### Python Operators (Basic Math)

```print(50 + 50)
   print(150 - 50)
   print(10 * 10)
   print(100 / 25)
```

* **+** is for **Addition**
* **-** is for **Subtraction**
* ***** is for **Multiplication**
* **/** is for **Division**

### Order of Operations
* Computers will follow PEMDAS. This means they will always complete **parenthesis** or groups first, then perform **exponents**, then **multiplication** and **division**, and **addition** and **subtraction** in the end.
* Follow PEMDAS for the following equations:
```5 + 30 * 20 #this will equal 605
   (5 + 30) * 20 #this will equal 700
   ((5 + 30) * 20) / 10 #this will equal 70
   5 + 30 * 20 / 10 #this will equal 65
```

### Challenge: How many Minecraft Boxes?
If I find 200 Mincraft Boxes and make 10 more a day for a year, but loose 3 of them a week. How many will I have?
* Here is a breakdown of the math:
```20 + 10 * 365 #how many boxes I find and make
   3 * 52 #how many boxes I loose
   3670 - 156 #how many boxes I find/make subtracting how many I lost
   20 + 10 * 365 - 3 * 52 #All the math in one line
```
* Here we can do it with variables (placeholders for values)
```foundBoxes = 20
   madeBoxes = 10
   lostBoxes = 3
   foundBoxes + madeBoxes * 365 - lostBoxes * 52
```

## Variables !!!

### Types of Variables
* String (words, letters, sentences, etc.)
* Integer (whole numbers)
* Float (decimals)
```name = "Barb"
   age = 23
   pi = 3.14
```

### Rules of Naming
* You cannot start with a **capitol letter**, **number**, **symbol** or **space**
* You cannot have spaces in names, instead use **camelCase** or an **under_score**

### Strings
* Strings are surrounded by single or double quotes ("" or '')
* Use double quotes if you are using contractions
```
firstHere = "Bryce & Kurt"
said = "said, 'There won't be vocabulary words today.'"
```
* Three single quotes in a row (''') will give multiple lines
```
joke = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
```

### Adding Strings
* Strings can only add strings
```name = "Barb"
   age = "23"
   hi = "Hello! My name is"
   iAm = "and I am"
   yrsOld = "years old."
   space = " "
   sentence = hi + space + name + space + iAm + space + age + space + yrsOld
   print(sentence)
```
* You can mask ints as strings by using **str()**
```name = "Barb"
   age = 23
   hi = "Hello! My name is"
   iAm = "and I am"
   yrsOld = "years old."
   space = " "
   sentence = hi + space + name + space + iAm + space + str(age) + space + yrsOld
   print(sentence)
```

### keyboard input & [Madlibs] Challenge (https://swantonpubliclibrary.org/sites/default/files/mad%20lib%20moon.jpg)
```x = input('enter your name.')
   print('Hello, ' + x)
```

