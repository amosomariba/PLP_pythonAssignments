def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Question 2

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${final_price:.2f}")
