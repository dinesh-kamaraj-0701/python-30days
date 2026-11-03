##Taxi fare engine. Ask for distance in km and whether it’s night (y/n). 
# Pricing: first 5 km at Rs. 60 per km, 
# next 15 km at Rs. 45 per km, anything beyond 20 km at Rs. 35 per km. 
# Add a 20% night surcharge if applicable. 
# Print an itemized breakdown by slab.
##Hint: this is a tiered calculation, much like tax slabs. 
# Compute how many km fall into each slab using min() and max(), 
# or if statements. Sketch it on paper with 27 km first.

#constant

total_fare=0
ikm=1
five_km_price=0
five_twenty_km=0
above_twenty=0
night_five_km=60+(60*.2)
night_fif_km=45+(45*.2)
night_twenty_km=35+(35*.2)


#input
distance=int(input("Enter the distance : "))
night_ind=input("Is it night travel (y/n): ")



#calculation
if night_ind=='n':
    while ikm<=distance:
        if ikm<=5:
            total_fare=total_fare+60
            ikm+=1
            five_km_price=five_km_price+60
        elif ikm<=20:
            total_fare=total_fare+45
            ikm+=1
            five_twenty_km=five_twenty_km+45
        elif ikm>20:
            total_fare=total_fare+35
            ikm+=1
            above_twenty=above_twenty+35
        else:
            break
elif night_ind=='y':
    while ikm<=distance:
            if ikm<=5:
                total_fare=total_fare+night_five_km
                ikm+=1
                five_km_price=five_km_price+night_five_km
            elif ikm<=20:
                total_fare=total_fare+night_fif_km
                ikm+=1
                five_twenty_km=five_twenty_km+night_fif_km
            elif ikm>20:
                total_fare=total_fare+night_twenty_km
                ikm+=1
                above_twenty=above_twenty+night_twenty_km
else :
    print("invalid input")
#output
print(f"The total fare for trips is : {total_fare}")
print(f"The total fare for first five km is: {five_km_price}")
print(f"The total fare for next 15 five km is: {five_twenty_km}")
print(f"The total fare above 20 km is: {above_twenty}")