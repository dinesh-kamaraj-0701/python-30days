# --- Constants ---
SLAB1_END_KM = 5
SLAB2_END_KM = 20
SLAB1_RATE = 60
SLAB2_RATE = 45
SLAB3_RATE = 35
NIGHT_SURCHARGE = 0.20

# --- Inputs ---
while True:
    distance_km = int(input("Distance in km: "))
    if distance_km >= 1:
        break
    print("Distance must be at least 1 km.")

while True:
    is_night = input("Night travel? (y/n): ").lower()
    if is_night in ("y", "n"):
        break
    print("Please enter y or n.")

# --- Calculation ---
slab1_fare = 0
slab2_fare = 0
slab3_fare = 0

for km in range(1, distance_km + 1):
    if km <= SLAB1_END_KM:
        slab1_fare += SLAB1_RATE
    elif km <= SLAB2_END_KM:
        slab2_fare += SLAB2_RATE
    else:
        slab3_fare += SLAB3_RATE

base_fare = slab1_fare + slab2_fare + slab3_fare
if is_night == "y":
    surcharge = base_fare * NIGHT_SURCHARGE
else:
    surcharge = 0
total_fare = base_fare + surcharge

# --- Output ---
print("=" * 36)
print(f"TAXI FARE FOR {distance_km} KM")
print("=" * 36)
print(f"Km 1-{SLAB1_END_KM}: Rs. {slab1_fare:,.2f}")
print(f"Km {SLAB1_END_KM + 1}-{SLAB2_END_KM}: Rs. {slab2_fare:,.2f}")
print(f"Km {SLAB2_END_KM + 1}+: Rs. {slab3_fare:,.2f}")
print("-" * 36)
print(f"Base fare : Rs. {base_fare:,.2f}")
print(f"Night (20%): Rs. {surcharge:,.2f}")
print(f"Total     : Rs. {total_fare:,.2f}")
print("=" * 36)