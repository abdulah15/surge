def power2(number):

    if (number == 0):
        return 0
    
    if ((number &(~(number - 1))) == number):
        return 1 

    return 0

number = int(input("Please Enter The Number = "))


if (power2(number)):
    print(" Number is a power of 2")
else: 
    print("Number is not a power of 2")
