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