country = input("Enter Your Country==>").title().rstrip().lstrip().strip()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(
        f"Your Country is {country}, Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(
        f"Your Country {country},Not Eligible For Discount And The Price Is ${price}")
