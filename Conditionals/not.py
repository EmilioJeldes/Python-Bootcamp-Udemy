age = 1

# not 2-8 years (2 dolars)
# not 65 > year (5 dolars)
# 10 dolars for everyone else

print(bool(age >= 2 and age <= 8))
print(bool(age >= 65))
# 	not		false 					false  = true
if not ((age >= 2 and age <= 8) or age >= 65):
    print("Pay 10 dolars")
