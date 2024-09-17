print ("SHANTO THOMAS: ")
print('''HELLO SHANTO
       WHATS GOING ON''')

name = input("Enter Your Namae: ")
print(name)
age = int(input("Enter Your Age"))
print(age)
exp1 = eval(input("enter exp"))
print(exp1)

# TYPECASTING
A = "Shanto"

print(type(A))
B = 23
print(type(B))



a = 123
b= 1.23

print(type(a))
print(type(b))
 
c = a+b
print (c) 
print (type(c))


# LOGICAL OPERATOR
print(3>2 and 7>3)
print(7>2 or 2>3)
print(not(7>2 and 2>3))


# Identity Operator is & is not
ab = 1234
ba = 1234
print(ab is ba)

aba = 1234
bab = "1234"

print(aba is not bab)


print(bin(10))
print(bin(8))
print(bin(2))

print(10 & 8)
print(10 | 8)
print(10 ^ 8)

word =  "SHANTO THOMAS"
print("H" in word)
 

marks= int(79)
if marks >= 80:
    print("Congarts u got the mobile phone ")
else:
    print("More hard work needed")
print("Next command")


Marks =  float(input("Enter your Marks:- "))
if Marks >= 90:
    print("top the class")

ratio = int(input("ENTER YOUR RATIO"))
if ratio == 8 : print("WORKING RATIO" , ratio)

need_multiple= int(input("Enter the multiple:- "))
need_range= int(input("Enter the range which u want in integer:- "))

for (jump) in range (need_range):
    print(need_multiple,"X", jump ,"=",need_multiple*jump)


n = 0 
multiple = int(input("Enter The Multiple:- "))
while n<= 10:
    print(n , "X", multiple , "=", n*multiple )
    n+=1

print("Adding 2 number" )

while True:
    add_one = int(input("Enter 1st number:-  "))
    add_second = int(input("Enter 2nd number:-  "))
    print("Your Answer is:- ",add_one + add_second)
    again = input("do you want to repeat the loop {YES OR NO}:- ")
    if again == "YES":
        break

