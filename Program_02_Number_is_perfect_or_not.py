n = int(input("Enter any number : "))
sum1 = 0
for i in range(1, n):
    if n % i == 0 :
        sum1 += i
if sum1 == n :
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
# Perfect numbers are the positive integers which are
# the sum of their proper divisors.
# The smallest perfect number is 6 (1+2+3)
