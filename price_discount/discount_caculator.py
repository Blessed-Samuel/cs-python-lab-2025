# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    Applies discount only if discount_percent >= 20
    """

    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price  # No discount applied.


# Test case
try:
    price = float(input("Please enter the original price of the item: "))
    discount_percent = float(input("Please enter discount percentage: "))
except ValueError:
    print("Please enter a valid numaric values.")
    exit()

# calculate final price
final_price = calculate_discount(price, discount_percent)

# output result
if discount_percent >= 20:
    print(f"Discount applied! Final price is: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
