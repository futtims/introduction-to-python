# The item's discount and stock status have been defined
discounted = False
lowStock = True

movingProduct = discounted or lowStock

promotion = not lowStock and discounted

print("Is the item eligible for promotion?", promotion)
