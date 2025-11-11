# Program to count digits in a number using while loop


num = int(input("Enter an integer: "))
n = abs(num)  
count = 0

# Special case for 0
if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10   # Remove the last digit
        count += 1

print("Number of digits:", count)
