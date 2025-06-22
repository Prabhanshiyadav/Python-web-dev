from mymathcalc import area_of_circle, circum_of_circle, area_of_sq

# Get the radius for the circle
radius = int(input('Enter the radius of the circle: '))
print(f'Area of Circle: {area_of_circle(radius)}')
print(f'Circumference of Circle: {circum_of_circle(radius)}')

# Get the side length for the square
side = int(input('Enter the side length of the square: '))
print(f'Area of Square: {area_of_sq(side)}')

