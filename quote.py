GST_RATE = 0.12
CHILD_PRICE_FACTOR = 0.5

# --- Inputs ---
customer_name = input("Customer name: ")
package_name = input("Package name: ")
adults = int(input("Number of adults: "))
children = int(input("Number of children: "))
nights = int(input("Number of nights: "))
adult_price = float(input("Adult price per night: "))
discount_percent = float(input("Discount %: "))

# --- Calculations ---
child_price = adult_price * CHILD_PRICE_FACTOR
subtotal = (adults * adult_price + children * child_price) * nights
discount = subtotal * discount_percent / 100
taxable_amount = subtotal - discount
gst = taxable_amount * GST_RATE
grand_total = taxable_amount + gst

# --- Output ---
print("=" * 40)
print(f"QUOTE FOR {customer_name} - {package_name}")
print("=" * 40)
print(f"Subtotal  : Rs. {subtotal:,.2f}")
print(f"Discount  : Rs. {discount:,.2f}")
print(f"Taxable   : Rs. {taxable_amount:,.2f}")
print(f"GST (12%) : Rs. {gst:,.2f}")
print(f"Total     : Rs. {grand_total:,.2f}")
print("=" * 40)