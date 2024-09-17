# PROBLEM 1
Number = int(input("Enter Number To Check:- "))
if Number >= 0:
    print("Number Is +ve")

else: 
    print("Number is -ve")

# problem 2
print("Checking If number is even or odd" )
check = int(input("Enter Number To Check:- "))
if check % 2 ==0:
    print("Number is even") 
else:
    print("Number is Odd")

#problem 3

hight =  int(input("Hight of the area:- "))
Lenghth = int(input("Lenghth of the lenghth:- "))
area = hight*Lenghth
print("Area of the input is:- ",area)

# problem 4
check_vowel = str(input("Enter the STRING:- "))
if  check_vowel in  "a e i o u" or check_vowel in "A E I O U"  :
     print("Countain")

else:
    print("Not Countain")