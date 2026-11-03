#constants
gst_rate=0.12
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
i=0
subtotal=0
peak_price_weekday=2500+(2500*0.25)
peak_price_weekend=3500+(3500*0.25)

#input
name = input("Enter your name : ")
arrival_day = input("Enter your arrival day (mon-sun) : ")
number_of_nights = int(input("Enter number of nights  (1-30) : "))
number_of_travellers = int(input("Enter number of travellers : "))
peak_season=input("Is it peak season? Enter y/n :").lower()
number_of_rooms=((number_of_travellers+2)//3)


#calculation
print(f"The number of rooms is {number_of_rooms}")
if arrival_day in days:
    day_index=days.index(arrival_day)
    if peak_season=='n':
        print("="*10)
        print("Not peak season")
        for i in range(number_of_nights):
            current = days[(day_index + i) % 7]
            if current in ("sat", "sun"):
                daily_price=0
                daily_price=(daily_price + 3500) * number_of_rooms
                subtotal +=daily_price
                print(f"weekend price for {days[(day_index + i) % 7]} is Rs. {daily_price}")
            else:
                daily_price=0
                daily_price =(daily_price + 2500) * number_of_rooms
                subtotal +=daily_price
                print(f"weekday price for {days[(day_index + i) % 7]} is Rs. {daily_price}")
        print(f" Subtotal for {number_of_nights} days is : Rs {subtotal}")
        grand_total=subtotal+(subtotal*gst_rate)
        print(f"Grand total for the stay inclusive of GST is {grand_total:,.2f}")
    elif peak_season=='y':
            print("="*10)
            print("Peak season")
            for i in range(number_of_nights):
                current = days[(day_index + i) % 7]
                if current in ("sat", "sun"):
                    daily_price=0
                    daily_price=(daily_price + peak_price_weekend) * number_of_rooms
                    subtotal +=daily_price
                    print(f"Weekend price for {days[(day_index + i) % 7]} is Rs. {daily_price}")
                else:
                    daily_price=0
                    daily_price =(daily_price + peak_price_weekday) * number_of_rooms
                    subtotal +=daily_price
                    print(f"Weekday price for {days[(day_index + i) % 7]} is Rs. {daily_price}")
            print(f"Subtotal for {number_of_nights} days is : Rs {subtotal}")
            grand_total=subtotal+(subtotal*gst_rate)
            print(f"Grand total for the stay inclusive of GST is {grand_total:,.2f}")
        
else:
    print("Invalid day of arrival !")