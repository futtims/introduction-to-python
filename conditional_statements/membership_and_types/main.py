# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

contains_raw = "raw" in description
contains_Imported = "Imported" in description

correct_price_type = type(price) == float
correct_count_type = type(count) == int

price_is_float = correct_price_type
count_is_int = correct_count_type

print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)

