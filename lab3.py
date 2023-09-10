#example1
# x=float(input("enter x: "))
# y=float(input("enter y: "))
# h=float(input("enter h: "))
# s=(x+y+h)/2
# area=s*(s-x)*(s-y)*(s-h)**0.5
# print(area)

#example2
#wt= float(input("Enter weight(in kg) : ")) #Get weight in kg
# ht = float(input("Enter height(in m) : ")) #Get height in m
# bmi = wt/(ht**2) #Calc bmi
# print(bmi)

#example3
# a,b,c=map(float, input("enter the three sides: ").split())
# if a+c>b:
#     print("yes it makes a triangle")
# elif a+b>c:
#         print("yes")
# else:
#     print("no it does not make a traingle")

#example4
# N=int(input("enter a three digit number: "))
# i1=N//100
# i2=(N//10)%10
# i3=N%10
# sum=i1+i2+i3
# print(sum)
# if sum%3==0:
#     print("sum is divisible by 3")
# else: 
#     print("sum is not divisible by 3")

#example5
N=int(input("enter a 5 digit number: "))
i5=N//10000
i4=(N//1000)%10
i3=(N//100)%10
i2=(N//10)%10
i1=N%10
print(i1,i2,i3,i4,i5)
n={i5,i4,i3,i2,i1}
if N==n:
    print("numbers are palindrome")
else:
    print("numbers are not palindrome")

#example7
# x=complex(input("enter first complex number: "))
# y=complex(input("enter second complex number: "))
# print(x+y, x*y)














    


