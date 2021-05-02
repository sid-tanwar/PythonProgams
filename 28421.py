a =-27
b = 3
print(a is b)
print(id(a))
print(id(b))

list = [1, 2, 3, 4, 5]

if b in list :
    print("The number {0} is available in the given list ".format(b))

else :
    print("The number {0} is not available in the given list".format(b))

c= 1100
d= 1101
print(c&d)

e=33
f=200

if f>e: print("f is greater than e")

elif f==e: print("f is equal to e")

else: print("f is smaller than e")

count = 0

while count < 5:
    print("{} is less than 5.".format(count))
    count =count+1
else:
    print("{} is not less than 5.".format(count))

for letter in "BVICAM":
    print("Current Letter : {}".format(letter))
else :
    print("First Loop Ended.")

colors=['RED', 'GREEN', 'BLUE']

for color in colors:
    print("Current Color : {}".format(color))

else :
    print("Second Loop Ended.")