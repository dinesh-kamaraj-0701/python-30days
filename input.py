person =int(input("person: "))

print(person//3)
print(person%3)
print((person+2)//3)
day=input("arrival day: ")
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

if day in days: 
    print(f"Day is  {day}") 
else:
    print("invalid")