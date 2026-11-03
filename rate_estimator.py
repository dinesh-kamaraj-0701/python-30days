# --- Constants ---
GST_RATE = 0.12
WEEKDAY_RATE = 2500
WEEKEND_RATE = 3500
PEAK_SURCHARGE = 0.25
GUESTS_PER_ROOM = 3
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# --- Inputs (each one validated before moving on) ---
customer_name = input("Customer name: ")

while True:
    arrival_day = input("Arrival day (mon-sun): ").lower()
    if arrival_day in DAYS:
        break
    print("Please enter one of: mon, tue, wed, thu, fri, sat, sun.")

while True:
    nights = int(input("Number of nights (1-30): "))
    if 1 <= nights <= 30:
        break
    print("Nights must be between 1 and 30.")

while True:
    travellers = int(input("Number of travellers: "))
    if travellers >= 1:
        break
    print("There must be at least 1 traveller.")

while True:
    peak_season = input("Peak season? (y/n): ").lower()
    if peak_season in ("y", "n"):
        break
    print("Please enter y or n.")

# --- Setup calculations ---
rooms = (travellers + GUESTS_PER_ROOM - 1) // GUESTS_PER_ROOM
if peak_season == "y":
    season_factor = 1 + PEAK_SURCHARGE
else:
    season_factor = 1
day_index = DAYS.index(arrival_day)
subtotal = 0

# --- Quote ---
print("=" * 44)
print(f"QUOTE FOR {customer_name}")
print(f"{nights} night(s), {travellers} traveller(s), {rooms} room(s)")
print("=" * 44)

for night in range(nights):
    current_day = DAYS[(day_index + night) % 7]
    if current_day in ("sat", "sun"):
        rate = WEEKEND_RATE
        day_type = "weekend"
    else:
        rate = WEEKDAY_RATE
        day_type = "weekday"
    night_cost = rate * season_factor * rooms
    subtotal += night_cost
    print(f"Night {night + 1} ({current_day}, {day_type}): Rs. {night_cost:,.2f}")

gst = subtotal * GST_RATE
grand_total = subtotal + gst

print("-" * 44)
print(f"Subtotal  : Rs. {subtotal:,.2f}")
print(f"GST (12%) : Rs. {gst:,.2f}")
print(f"Total     : Rs. {grand_total:,.2f}")
print("=" * 44)