# Yvonne Aime
# COP2500C 
# Math Library 
# July 26 2023

import math

# Functions needed to know

# Rounding functions
print(round(3.6))

# Rounding two-digits 
print(round(3.445, 2))
print(round(3.40001, 2))

# Always Rounds UP
# -Rounds to 4
print(math.ceil(3.3))

# Always Rounds Down
# -Rounds to 99
print(math.floor(99.99999))

# Square root - turns numbers into floats
print(math.sqrt(64))

# Power - 2 to the third power 
print(2 ** 3) # same thing as below
print(math.pow(2, 3))

# Absolute Values
print( math.fabs(4))
print( math.fabs(-3))

rads = math.radines(270)
cof = rads / math.pi
print(cof, "*PI")
