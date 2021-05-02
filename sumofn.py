n = int(input("Enter a number : "))
temp=n
sum = 0

while(n>0) :
    sum = sum + n
    n = n-1
print("The sum of {} natural numbers is {}. ".format(temp, sum))

