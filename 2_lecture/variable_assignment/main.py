# simple assignment
name = "Anton"
age = 10

print(name, age)

# assignment in one row
name, age = "Anton", 10

print(name, age)

# swap variables
name, age = age, name

print(name, age)

# unpacking from tuple
name, age = ("Anton", 10)

print(name, age)

# unpacking from list
name, age = ["Anton", 10]

print(name, age)

# unpacking from list
name_1, name_2, name_3, name_4 = ["Anton", "Ivan", "Dima", "Kolya"]

print(name_1, name_2, name_3, name_4)

# hard unpacking from list
first, *_, last = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

print(first, last)

# hard unpacking from list
first, second, *_, last = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

print(first, second, last)

# hard unpacking from list
_, *meaningful_names, _ = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

print(meaningful_names)

# hard unpacking from list
*names, _, _, _, _, _ = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

print(names)

# hard unpacking from list
_, _, _, _, _, _, *names = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

print(names)



