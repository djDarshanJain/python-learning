age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

if age>=18:
    if cgpa>=7.5:
        print("you are selected.")
    else:
        print("cgpa is too low.")
else:
    print("you are underage.")

print("program ended")