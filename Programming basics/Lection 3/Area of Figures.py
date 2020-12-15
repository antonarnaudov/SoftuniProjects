from math import pi
shape = input()

if shape == 'square':
    sideA = float(input())
    area = sideA ** 2
elif shape == 'rectangle':
    width = float(input())
    lenght = float(input())
    area = width * lenght
elif shape == 'circle':
    r = float(input())
    area = pi * (r**2)
elif shape == "triangle":
    h = float(input())
    b = float(input())
    area = h * (b/2)

print(f'{area:.3f}')

