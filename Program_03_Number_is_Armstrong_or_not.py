# An Armstrong number is a positive m-digit number that
# is equal to the sum of the m th powers of their digits.
no = int(input("Enter any number to check : "))
no1 = no
sum = 0
while no>0 :
    ans = no % 10
    sum = sum + (ans**len(str(no1)))
    no = int (no/10)
if sum == no1:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
