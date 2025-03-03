import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ''
    if n < 4:
        print('The triangle height should be at least 4.')
    else:
        print ('*')
        for i in range (n - 2):
            print ('*', end = '')
            for j in range (i):
                print (' ', end= '')
            print ('*', end = '')
            print()
        for i in range (n):
            print ('*', end = '')

    return result.rstrip()

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result =''
    if n < 3:
        print('The pyramid height should be at least 3.')
    else:
        for i in range (n):
            for j in range (i):
                print(' ', end = '')
            for j in range (i, n - 1):
                print ('*' , end= '') 
            for j in range (i, n):
                print ('*', end = '')
            print()

    return result.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()