print('Module 1 ')
numa = float(input("Enter first number : "))
numb = float(input("Enter second number : "))
numc = float(input("Enter third number : "))
mod1ask = input("Choose operation(+ to add, * to multiply, ^ to find average number) : ")

if mod1ask == "+" :
    mod1act = numa + numb + numc
    print('Sum of the numbers you wrote is : ', mod1act)

elif mod1ask == "*" :
    mod1act = numa * numb * numc 
    print("The multiplication of your numbers is : ", mod1act)

elif mod1ask == "^" :
    mod1act = (numa + numb + numc) / 3
    print("The average number is : ", mod1act)

else: 
        print("Error")


print("Module 2 ")
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))
mod2ch = input("Choose what to find(+ to find the biggest, - to find the smallest, = to find the middle number) : ")


if c <= a >= b:
    maxNUM = a
    if b >= c:
        avenum = b
        minNUM = c
    else:
        avenum = c
        minNUM = b
elif a <= b >= c:
    maxNUM = b
    if a >= c:
        avenum = a
        minNUM = c
    else:
        avenum = c
        minNUM = a
else:
    maxNUM = c
    if a >= b:
        avenum = a
        minNUM = b
    else:
        avenum = b
        minNUM = a

if mod2ch == '+':
    print("The biggest number is : ", maxNUM)
elif mod2ch == '-': 
    print('The smallest number is : ', minNUM)
elif mod2ch == '=':
    print('The middle number is : ', avenum)
else :
    print("Error")

print('Module 3')
mod3meter = float(input('Enter meters : '))
mod3ch = input('Choose in what to convert(1 to convert to mm, 2 to km) : ')
if mod3ch == "1":
    print(mod3meter, 'm = ', mod3meter * 1000, 'mm')
elif mod3ch == "2":
    print(mod3meter, 'm = ', mod3meter / 1000, 'km')
else :
    print('Error') 


    








