num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2 # returns quotient with decimal part
floor_div = num1 // num2 # returns quotient with no decimal part
power = num1 ** num2 # returns num1 ki power num2
modulus = num1 % num2 # returns remainder
print('Sum of ', num1, 'and', num2, 'is : ', add)
print('Difference of ', num1, 'and', num2, 'is : ', dif)
print('Product of ', num1, 'and', num2, 'is : ', mul)
print('Division of ', num1, 'and', num2, 'is : ', div)
print('Floor Division of ', num1, 'and', num2, 'is : ', floor_div)
print('Exponent of ', num1, 'and', num2, 'is : ', power)
print('Modulus of ', num1, 'and', num2, 'is : ', modulus)
