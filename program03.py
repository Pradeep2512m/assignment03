def ispalindrome(x):
    return x == x[:: -1]
a = "rotator"
result = ispalindrome(a)
if result:
    print("palindrome")
else:
    print("not a palindrome")