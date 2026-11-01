GST=12
destination = input("Destination: ")
nights = int(input("Nights: "))
rate_per_night = float(input("Rate per night: "))
bill=nights*rate_per_night
total=bill+(bill*(GST/100))

print(f"Quote for {destination}: {nights} //n nights x Rs. {rate_per_night:,.2f} = Rs. {total:,.2f} including GST")