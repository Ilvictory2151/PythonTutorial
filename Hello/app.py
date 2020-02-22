print("Hello World")
print("My name is Victory T. Tamang.")
print("Testing")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

age = ("14")
print("My name is Victory T. Tamang and I'm " + age + "-years-old.")

name = ("Victory T. Tamang")
print("I'm " + name + " and I live in California")

location = ("California")
year = ("2005")
print("I'm " + name + " and was born in " + year + ". I live currently live in " + location + ".")

print(name.upper())
print(name.lower())

print(name.isupper())
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name + " was born in 2005.")

print(name)
print(name.index("V"))
print(name.index("i"))
print(name.index("c"))
print(name.index("t"))
print(name.index("o"))
print(name.index("r"))
print(name.index("y"))
print(name.index(" "))
print(name.index("T"))
print(name.index("a"))
print(name.index("m"))
print(name.index("a"))
print(name.index("n"))
print(name.index("g"))

my_num = -5
print(abs(my_num))
print(pow(3, 5))
print(min(3, 5))
print(max(3, 5))
print(round(3.14156))
print(round(3.7))

from math import*

print(max(3.7, pow(3.7, 20)))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))
print(sqrt (pow(36, 6)))

friends = ["Kevin", "Karen", "Jim"]
friends[1] = "Mike"
print(friends[1:])

lucky_numbers = [4,8,15,16,23,42]
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends1.append("Creed")
friends1.insert(1, "Kelly")
friends1.reverse()
print(friends1)
print(friends1.index("Karen"))

friends2 = friends1.copy()
print(friends2)

coordinates = [(4, 5), (6, 7), (80, 34)]
coordinates[1] = 10
print(coordinates[0])

def say_hi(name, age):
    print("Hello " +name+ "you are are " +str(age)+ ".")

print("Top")
say_hi("Mike", 35)
say_hi("Steve", 70)
print("Bottom")



color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " +color)
print(plural_noun+ " are blue")
print("I love " +celebrity)

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You're " + age + "!")

num1 = input("Enter a number: ")
num2 = input("Enter another a number: ")
result = int(num1) + int(num2)
print(result)

num1 = input("Enter a number with a decimal: ")
num2 = input("Enter another a number with a decimal: ")
result = float(num1) + float(num2)
print(result)

