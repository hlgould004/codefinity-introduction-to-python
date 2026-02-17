seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
#Define over stock risk
overstock_risk = (seasonal and current_stock > high_stock_threshold)
print(overstock_risk)
#Define if discount is eligible
discount_eligible = (not selling_well  and not on_sale)
print(discount_eligible)
#Define make discount
make_discount = (overstock_risk or discount_eligible)
print(make_discount)
#Final print out
print("Should the item be discounted?", make_discount)