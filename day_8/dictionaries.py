### Day 8 : Dictionaries ###

## Exercises ##

# 1. Create an empty dictionary called dog

dog = dict()
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary

dog = {
    "name": "Manga",
    "color": "Red",
    "breed": "European",
    "legs": 4,
    "age": 4  # we use : not =
}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys

student = {
    "first_name": "Ines",
    "last_name": "Amd",
    "gender": "Female",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Data", "AI", "SEO"],
    "country": "France",
    "city": "Colombes",
    "address": "allée de l'île m"
}
print(student)

# 4. Get the length of the student dictionary

print(len(student))  # 9

# 5. Get the value of skills and check the data type, it should be a list

print(type(student.get("skills")))  # it's a list

# 6. Modify the skills value by adding one or two skills

student["skills"].extend(["R", "Python"])
print(student["skills"])

# 7. Get the dictionary keys as a list

student_keys = student.keys()
print(student_keys)

# 8. Get the dictionary values as a list

student_values = student.values()
print(student_values)

# 9. Change the dictionary to a list of tuples using items() method

print(student.items())  # gives a list of tuples

# 10. Delete one of the items in the dictionary

del student["address"]
print(student.keys())

# 11. Delete the student dictionary

del student

## Exercises from Ecosia ##

# 1. Create an empty dictionary called car

car = dict()
print(car)

# 2. Add brand, model, year, color, features to the car dictionary

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "color": "blue",
    "features": ["Air conditioning", "Bluetooth", "Backup camera"]
}
print(car)

# 3. Get the length of the car dictionary

print(len(car))

# 4. Get the value of features and check the data type, it should be a list

print(type(car["features"]))  # <class 'list'>

# 5. Modify the features value by adding one feature

car["features"].append("Sunroof")
print(car["features"])

# 6. Get the dictionary values

print(car.values())

# 7. Get the dictionary keys

print(car.keys())

# 8. Change the dictionary to a list of tuples using items() method

print(car.items())

# 9. Delete one of the items in the dictionary (color)

del car["color"]

# 10. Print the keys after deletion

print(car.keys())

# 11. Delete the car dictionary

del car

# I tried to print car after deletion (will raise an error because car no longer exists)
# print(car)  # NameError: name 'car' is not defined