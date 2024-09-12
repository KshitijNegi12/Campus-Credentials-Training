def myfunc(name):
    print(f"Hello, {name}")

# add 
def add(a,b):
    print("addition:",a+b)

# subtract
def sub(a,b):
    print("sub:",a-b)

# armstrong
def armstrongnumber(num):
    temp=num
    sum=0
    count=0
    while temp>0:
        sum=sum+(temp%10)**count
        temp=temp//10
    if(sum==num):
        print("entered number is armstrong no:",num)
    else:
        print("entered number is not armstrong no:",num)

# palindrome
def palindrome(num):
    temp=num
    rev=0
    while temp>0:
      rev =  rev*10 + temp%10
      temp=temp//10
    if rev == num:
       print("entered number is palindrome:",num)
    else:
       print("entered number is not palindrome:",num)

# Factorial 
def factorial(num):
    if num < 1: return 1
    return factorial(num-1) * num

# Reverse
def reverse(num):
    temp=num
    rev=0
    while temp>0:
      rev =  rev*10 + temp%10
      temp=temp//10
    return rev