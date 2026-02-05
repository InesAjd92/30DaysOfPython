### Day 8 

# Exercises 

# 1/

dog = dict()
print(dog)

# 2/ 

dog = {
    "name" : "Manga",
    "color" : "Red",
    "breed" : "European",
    "legs" : 4, 
    "age" : 4} # we use : not =

print(dog) 

# 3/

student = {
    "first_name" : "Ines",
    "last_name" : "Amd",
    "gender" : "Female",
    "age" : 25,
    "maritale_status" : "Single",
    "skills" : ["Data", "IA", "SEO"],
    "country" : "France",
    "city" : "Colombes",
    "adress" : "all de l'ile m"
}

print(student)

# 4/

print(len(student)) #9

# 5/

print(type(student.get("skills"))) #yes, this is a list

# 6

 # i have to to like that d["blabla"]. append 

student["skills"].extend(["R", "Python"])

#extend for individuals elements instead of append!

print(student["skills"])

# 7/

student_keys = student.keys()
print(student_keys)

# 8/

student_values = student.values()
print(student_values)

# 9/

print(student.items()) #gives a list of tuples 

# 10/

del student["adress"]
print(student.keys())

# 11/ 

del student 


### Exercises from ecosia 

# 1/ 

car = dict()
print(car)

# 2/

car = {
    "brand" : "Toyota", 
    "model" : "Corolla", 
    "year" : 2020,
    "color" : "blue",
    "features" : ["Air conditioning", "Bluetooth", "Backup camera"]
}

print(car)

# 4/ 

print(len(car))

# 5/

print(type(car["features"])) #list

# 6/

car["features"].append("Sunroof")
print(car["features"])

# 7/

print(car.values())

# 8/

print(car.keys())

# 9/ 

print(car.items())

# 10/

del car["color"]

# 11/ 

print(car.keys())

# 12/

del car 

# 13/

print(car) #car is not defined because doesnt exist anymore