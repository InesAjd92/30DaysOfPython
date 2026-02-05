### Day 3 : Operators ###

## Exercises ## 

# Level 1 : 

# 1. Declare your age as integer variable'''
'''age = int(25)
print(age)

# 2. Declare your height as a float variable

height = float(157)
print(height, "cm")

# 3. Declare a variable that store a complex number

complex_number = 12j - 4

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# The formula is = 0.5 * b * h

base = int(input("Enter base :"))
height = float(input("Enter height:"))
area_of_triangle = 0.5 * base * height

print("The area of the triangle is", area_of_triangle)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# The formula is = a + b + c

a = int(input("a is :"))
b = int(input("b is :"))
c = int(input("c is :"))

perimeter = a + b + c 

print("The perimeter of the triangle is : ", perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))


length = int(input("The length of the rectangle is : "))
width = int(input("The width of the rectangle is : "))

area_of_rectangle = length * width
print("The area of the rectangle is : ", area_of_rectangle)

perimeter_of_rectangle = 2*(length+width)
print("The perimeter of the rectangle is :", perimeter_of_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
radius = int(input("The radius is"))

area_of_circle = pi*radius*radius
print("The area of the circle is", area_of_circle)

circumference_of_circle = 2*pi*radius
print("The circumference of the circle is :", circumference_of_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# It's an equation like y = mx+b

# m is the slope
# b is the y-intercept

# So here : y = 2x-2

# m = 2
# y = -2

# To find what is the y-intercept I need to find y when x = 0

# y = 2*0-2
# y = -2
# y-intercept = (0,-2)

# To find what is the x-intercept I need to find x when y = 0

# 0 = 2x -2
# 2 = 2x
# 2/2 = x
# x = 1
# x-intercept = (1,0)

# Let's do this with python

m = 2 # slope
b = -2 # b is the y-intercept 
slope = m

y_intercept = (0, b) # for y the 0 is first

x_intercept_x = -b/m
x_intercept = (x_intercept_x, 0)

print("The slope is", slope)
print("The y_intercept is ", y_intercept, "and the x_intercept is ", x_intercept)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

y1 = int(input("The y1 is "))
y2 = int(input("The y2 is "))
x1 = int(input("The x1 is "))
x2 = int(input("The x2 is "))

slope = m
m = (y2-y1)/(x2-x1)

print("The slope is :", m)

# For (2,2) and (6,10) the slope is 2.

# Now, I will calculate the euclidian distance.

euclidian_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The euclidian distance is ", euclidian_distance)

# So, the euclidian distance for those points is 8.94427

# 10. Compare the slopes in tasks 8 and 9.

# The slopes in tasks 8 and 9 are the same. 

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0. '''

x = int(input("Try some x "))
y = (x)**2 + 6*(x) + 9
print(y)


# g pas réussi car c chiat

# 12 """

""" print(len("python"))
print(len("dragon"))

print("python" == "dragon") 

#13/

print("on" in "python" and "on" in "dragon")

#14/
print("jargon" in "I hope this course is not full of jargon")

#15/ 
print("on" not in "python" and "on" not in "dragon")

#16/

lenght_python = len("python")
print(lenght_python)
print(float(lenght_python))
print(str(lenght_python))

# 17

# test 1
remainder = 0
x = int(input("Choose an x:"))
even_number = (x / 2 and remainder is 0)
print(x, "is an even number", even_number)

# test 2 
# formula for the remainder = a%b

even_number = x/2 == 0
print(x, "is an even number", even_number)
 """
# it works! :)

# 18 / floor_division = a // b
'''
print(7//3)
print(int(2.7))

print((7//3) == int(2.7)) # so it's true

#19/

print("10" == 10) # false bc str and int

#20/

print(int(9.8) == 10) # false 

# 21 / 
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter hours"))
rate_per_hour = int(input("Enter rate per hour"))
weekly_earning = hours * rate_per_hour

print("Your weekly earning is", weekly_earning)

# 22/

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

number_of_years = int(input("Enter number of years you have lived"))
number_of_seconds = 31536000 * number_of_years #number of seconds for one year
print("You have lived for", number_of_seconds)

# 23/ 

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
#idk if it was the right method 
'''

