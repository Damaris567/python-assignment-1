def calculate_discount(price, discount_percent):
    if discount_percent >20:
        discount=(discount_percent/100)*price 
        final_price= price-discount
        return final_price
    else:
        return price
    

price = 1000
discount_percent = 25
final_price = calculate_discount(price,discount_percent)
print (final_price)

