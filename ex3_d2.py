i=1
free_breakfast=0
for i in range(1,15):
    if i%2==0:
        print(f"Free breakfast for {i}'th night")
        i+=1
        free_breakfast+=1
    else:
        print(f"Standard breakfast for {i}'th night")
        i+=1
print(f"Tota free breakfast provided for {free_breakfast} nights")