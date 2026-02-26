### Day 24 : Statistics ###

## Exercises ##

# Level 1 : 

# 1. 

import numpy as np 
print('numpy:', np.__version__)
print(dir(np))

# create in numpy array 

python_list = [1,2,3,7,8,9]
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

numpy_array_from_lst = np.array(python_list)
print(numpy_array_from_lst)

# create float

numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2) # array([1., 2., 3., 4., 5.])

# create boolean 

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# create multidimensional array

numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# to reconvert an array (np) to a list (python) we can use tolist

np_to_list = numpy_array_from_lst.tolist()
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Numpy array from tuple 

python_tuple = (1,2,3,4,5)
numpy_array_from_tuple = np.array(python_tuple)
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

# Shape of numpy array 

# With the shape method we can know the shape of the array (as a tuple)
# The first is row and the second is the column
# If the array is unidimensional it return the size of the array

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape) # unidimensionnel

numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape) # should be (3,3), yes !

three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape) # should be (3,4), yes !

# Data types : 

# There is a lot of data types : Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype) # int64
print(float_array)
print(float_array.dtype) #float64

# Size of numpy array

# In numpy to know the number of items in a numpy array list we use size

two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])
print('The size:', numpy_array_from_lst.size) # 5
print('The size:', two_dimensional_list.size)  # 3

# Mathematical operations with numpy

# Addition

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)

ten_plus_original = numpy_array_from_list  + 10 # loop through each element 

print(ten_plus_original)

# Subtraction

numpy_array_from_list = np.array([1, 2, 3, 4, 5])

print('original array: ', numpy_array_from_list)

ten_minus_original = numpy_array_from_list  - 10

print(ten_minus_original)

# Multiplication 

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_times_orginal = numpy_array_from_list * 10
print(ten_times_orginal)

# Division 

numpy_array_from_list = np.array([1,2,3,6,6])
ten_times_orginal = numpy_array_from_list / 10
print(ten_times_orginal)

# Modulus; Finding the remainder

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# Floor division: the division result without the remainder

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# Exponential is finding some number the power of another:

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

# Check data types  with dtype

numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Converting types, also with dtype 

# int to float 

numpy_int_arr = np.array([1,2,3], dtype = "float")
print(numpy_int_arr)

# float to int 

numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

# int to boolean 

numpy_int_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr)

# int to str 

numpy_int = np.array([1,2,4])
numpy_int_to_str = numpy_int.astype("str")
print(numpy_int_to_str.dtype)


## Multi-dimensional arrays 

# 2 Dimension Array

two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Getting items from a numpy array 

first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]

print('First row:', first_row) # its not the first element, its the row itself!
print('Second row:', second_row)
print('Third row: ', third_row)

first_column = two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]

print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)

# Slicing numpy array 

first_two_rows = two_dimension_array[0:2, 0:2]
print(first_two_rows)

# to reverse the rows and the arrat we use [::]

# To reverse the row and column positions ! 

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array = two_dimension_array[::-1,::-1]
print(two_dimension_array)

# Handle NA 
    
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# numpy zeroes 
# numpy.zeros(shape, dtype=float, order='C')
# allow to create an arroy full of zeroe

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# could be full of ones also 

numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

twoes = numpy_ones * 2
print(twoes)

# Reshape

# numpy.reshape(), numpy.flatten()

first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)

reshaped = first_shape.reshape(3,2) # 3 rows two columns
print(reshaped)
 
flattened = reshaped.flatten()
print(flattened) # list

## Horitzontal Stack

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two) # each element at each position are additioned

# with hstack we can join the lists (horizontal)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# with vstack for vertical 

print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# Generate random numbers 

random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5) # we want 5
print(random_floats)

# if we want an integer we use randint (seen earlier in the class)

random_int = np.random.randint(0, 11) # between 0 and 10
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array

random_int = np.random.randint(2,12, size = 4) # 4 number in one row 
print(random_int)

# if we want a multidimensional array we should specify the size between ()

random_int = np.random.randint(2,10, size=(3,3))
print(random_int) # three rows three columns

# Generate numbers who follow a normal distribution 

# np.random.normal(mean, ecart type, size)
""""
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
"""
# Numpy and stats

import matplotlib.pyplot as plt # usefool tool to create graphs in pyton
import seaborn as sns # extension of matplotlib
"""
sns.set_theme() # set theme by defaults 
plt.hist(normal_array, color="grey", bins=50) # create an hist with the data of normal_array, the bars are in grey and the bucket are 50
plt.show() # to see it
"""


# Matrix with numpy

# matrix is a two dimensional array

# for example 

matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(matrix)

# or 

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float)) # we only take 1, we want 4 rows and for Columns, 1 will be float

print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2

print(four_by_four_matrix)

# The equivalent to range in numpy is arange 

# numpy.arange(start, stop, step)

whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers) #whithout 0

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

# With linspace we can creat sequence of nb evenly spaced 

example = np.linspace(1.0, 5.0, num=10)
print(example) # if we dont want the last value we can use endpoint=False

# If we want even spaced numbers on a log scale, we can use logspace
# numpy.logspace(start, stop, num, endpoint)

log_arr = np.logspace(2, 4.0, num=4)
print(log_arr)

# to check the size of an array

x = np.array([1, 2, 3], dtype=np.complex128)
print("Nb of elements :", x.size)
print("size of one element (oct) :", x.itemsize)

# indexation and slicing 

np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)

print('first row :', np_list[0])
print('second row :', np_list[1])

print('first column :', np_list[:, 0])
print('second column :', np_list[:, 1])

# Stats functions 

two_dimension_array = np.array([[1, 2, 3],
                                [4, 55, 44],
                                [7, 8, 9]])

print('Min:', two_dimension_array.min())
print('Max:', two_dimension_array.max())
print('Mean:', two_dimension_array.mean())
print('Std:', two_dimension_array.std())

# by column we use amin and (axis=0) and byrow (axis=1)
print('Min by column:', np.amin(two_dimension_array, axis=0))
print('Max by column:', np.amax(two_dimension_array, axis=0))

print('Min by row:', np.amin(two_dimension_array, axis=1))
print('Max by row:', np.amax(two_dimension_array, axis=1))

# To create repeating sequence we can use tile 

a = [1, 2, 3]

print('Tile:', np.tile(a, 2))     # repeat all the list 2 times
print('Repeat:', np.repeat(a, 2)) # repeat all element of the list two times 

# Generate random numbers 

# between 0 and 1 

one_random_num = np.random.random()
print(one_random_num)

# if we want them in a arraty we should specify the size in []

r = np.random.random(size=[2, 3]) # 2 rows three columns
print(r)

# Random choises in a list 

vowels = ['a', 'e', 'i', 'o', 'u']
random_choices = np.random.choice(vowels, size=10) # we want 10 choices
print(random_choices)

# if we want the choices to follow a normal disrubtion we can do that 

rand_normal = np.random.normal(loc=5, scale=0.5, size=12) # means mean of the normal distribution, centred between 5, σ and size 
print(rand_normal)

# lets do some stats in those random normal numbers

import scipy.stats as stats

print('Min:', np.min(rand_normal))
print('Max:', np.max(rand_normal))
print('Mean:', np.mean(rand_normal))
print('Median:', np.median(rand_normal))
print('Mode:', stats.mode(rand_normal))
print('Std:', np.std(rand_normal))

# lets do an histogram 

"""
sns.set_theme()  # the them
plt.hist(rand_normal, color='grey', bins=21) # we create the graph

plt.xlabel('values')
plt.ylabel('frequency')
plt.title('Histogram of the normal distribution')
plt.show()
"""

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# numpy.dot(x, y, out=None)

f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(np.dot(f, g))  # 1*4 + 2*5 + 3*6 = 32

# Matmul: matruc product of two arrays
# rows of A with column of B 
# ex : for 0,0 : we do 1*5 + 2*7

h = np.array([[1, 2],
              [3, 4]])
i = np.array([[5, 6],
              [7, 8]])

result = np.matmul(h, i)
print(result)

# List comprehension

new_list = [x + 2 for x in range(0, 11)]
print(new_list)

# with numpy

np_arr = np.array(range(0, 11))
print(np_arr + 2)

# Linear equation
# ex with pressure pressure=2×temp+5

temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5 
print(pressure)

# lets see that with matplotlib 

"""
plt.plot(temp, pressure)
plt.xlabel('Temperature in °C')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
"""