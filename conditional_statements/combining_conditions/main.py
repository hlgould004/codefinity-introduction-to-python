# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = not(discounted) or lowStock
print(movingProduct)

promotion = not movingProduct
print("Is the item eligible for promotion?", promotion)


