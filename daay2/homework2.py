# p1
age = int(input("enter your age :"))

if age>=18 :
    print("you are eligible to vote")
else :
    print("you are not eligible to vote")

# p2
num = int(input("enter your number :"))

if num>0 :
    print("number is positive.")
elif num==0:
    print("number is zero .")
else :
    print("number is negative.")

# p3
marks = int(input("enter your marks :"))

if marks>=90 :
    print("Grade A ")
elif marks>=75:
     print("Grade B ")
elif marks>=60:
     print("Grade C")
else :
     print("fail")


# p4
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age>=21:
    if salary>=30000:
        print("loan approved.")
    else:
        print("loan rejected.")
else:
    print("loan rejected.")

