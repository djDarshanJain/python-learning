age=int(input("enter your age :"))
cgpa=float(input("enter your cgpa :"))

print("eligible for interview :",age>= 18 and cgpa >=7.5)
print("can apply : ",age>=18 or cgpa>= 7.5)
print("minor : ",not(age>=18))