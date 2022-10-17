#Importing Imagenary Numbers
import cmath
#User input, and float changes to munber, not sting
a = float(input('A is: '))
b = float(input('B is: '))
c = float(input('C is: '))
# Math
x = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a
y = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a
#Desplaying the Solutions
print('The Solutions are: ')
print(x)
print(y)