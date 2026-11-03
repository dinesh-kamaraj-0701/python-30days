total=0.0
number=0
while True:
    exp=input("Expense or ‘done’ :")
    if exp=="done":
        print(f"Expense is {total}")
        break
    else:
        total=total+float(exp)
        number +=1

if total==0:
    print("no expense")
else:
    average=total/number
    print(f"Total expense is {total} and average is {average:,.2f}")

