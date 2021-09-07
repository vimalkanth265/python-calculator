def addition():
    sum=FirstNumber + SecondNumber
    print("Addition of two numbers is ",sum)

def subtraction():
    sub=FirstNumber-SecondNumber
    print("Subtraction of two numbers is :",sub)

def multiplication():
    multiple=FirstNumber*SecondNumber
    print("Multiplication of two numbers is :",multiple)

def division():
    div=FirstNumber/SecondNumber
    print("Division of two numbers is :",div)

def modulo():
    modules=FirstNumber%SecondNumber
    print("modulo of two numbers is :",modules)


def exponential():
        global exponentialNumber
        exponentialNumber**=2
        print("Exponential of given number :",exponentialNumber)

def default():
    print("Enter the valid answer")




print("1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.modulo\n 6.exponential")
n=int(input("Enter the option : "))
if n==6  :
        exponentialNumber=float(input("Enter the value : "))
        exponential()
else :
    if n>6:
        print("Your option is not in a list")
    else :
        FirstNumber=float(input("Enter the first number :"))
        SecondNumber=float(input("Enter the second number :"))
        option={
            1:addition,
            2:subtraction,
            3:multiplication,
            4:division,
            5:modulo

        }
        
        option.get(n, default)()




