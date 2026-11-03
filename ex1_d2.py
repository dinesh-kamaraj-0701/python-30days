age=int(input("Please enter your age : "))
if age < 5 :
    print("Free")
elif age < 12 :
    print("Child")
elif age < 60 :
    print("Adult")
elif age >= 60 :
    print("Senior")
else:
    print("Invalid or 0")