def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt user for input
price = int(input("Enter price: "))
discount_percent_input = input("Enter discount percent (leave blank for no discount): ")

# Check for empty input of discount percent
if discount_percent_input.strip() == "":
    discount_percent = 0  # No discount applied
else:
    discount_percent = int(discount_percent_input)

final_price = calculate_discount(price, discount_percent)

# Display the result after checking if the discount is 0
if discount_percent == 0:
    print("No discount applied. The original price is:", price)
else:
    print("The final price after applying the discount is:", final_price)