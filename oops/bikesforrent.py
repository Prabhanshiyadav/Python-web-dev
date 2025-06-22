# bikesforrent.py

from oops.bikes import Bikes

brnd = input('Brand: ')
rpd = int(input('Rent per day: '))

# Create object with brand and rent
bkobj = Bikes(brand=brnd, rent=rpd)

days = int(input('No. of days: '))

# Output
print(f'Bike {bkobj.bikename} for {days} days costs ₹{bkobj.calculate_rent(days)}')
