import math

first_name = 'Python'
last_name = '30-Days of python'
full_name = 'Python 30-Days of python'
country = 'Indonesian'
city = 'Jakarta'
age = 18
year = 2021
is_married = False
is_true = True
is_light_on = False
name, long_name, nickname = 'lleans', "lleans's", "lleans"

print(first_name, type(first_name))
print(last_name, type(last_name))
print(full_name, type(full_name))
print(country, type(country))
print(city, type(city))
print(age, type(age))
print(year, type(year))
print(is_married, type(is_married))
print(is_true, type(is_true))
print(is_light_on, type(is_light_on))
print(name, type(name))
print(long_name, type(long_name))
print(nickname, type(nickname))

print("Length First Name:", len(first_name))
print("Length Last Name:", len(last_name))

num_one, num_two = 5, 4
print(num_one, num_two)
_total = num_one + num_two
print(_total)
_diff = num_two - num_one
print(_diff)
_product = num_two * num_one
print(_product)
_division = num_one / num_two
print(_division)
_reaminder =  num_two % num_one
print(_reaminder)
variable_exp = num_one ** num_two
print(variable_exp)
_floor_division = num_one // num_two
print(_floor_division)

# Circle
circle_radius = 30
area_of_circle = math.pi * circle_radius ** 2
print(area_of_circle)
circum_of_circle = 2 * math.pi * circle_radius
print(circum_of_circle)

# Circle-input
circle_radius_input = int(input("jari-jari lingkaran: "))
area_of_circle_input = math.pi * circle_radius_input ** 2
print(area_of_circle_input)

first_name = input("First Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input("Age: ")
print(first_name, last_name, country, age)
