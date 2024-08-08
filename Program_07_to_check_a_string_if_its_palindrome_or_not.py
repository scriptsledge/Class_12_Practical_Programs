def ispalindrome(s):
    return s== s[::-1]
s = str(input("Enter the string data : "))
ans = ispalindrome(s)

if ans :
    print("yes")
else:
    print("no")