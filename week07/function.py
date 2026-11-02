# exercise 1

 # define calculate tax function

def calculate_tax(sale, tax_rate):
    return sale * tax_rate

# Calling the fuinction
tax1=calculate_tax(100, 0.07)
tax2=calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}")
print(f"Tax on 250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

# exercise 2

def apply_discount(price, tier):
    if tier == "Gold":
        return price * 0.85 
    elif tier == "Silver":
        return price *  0.90
    elif tier == "Bronze":
        return price * 0.95
    else:
        return price

    # Calling the function

    price=200
    tiers=["gold", "silver", "bronze", "none"]

    for tiers in tiers:
     print(f"{tier}: ${apply_discount(price, tier):.2f}")


     # exercise 3
      #write it out manually first, then refactor to use a function

    discounted=apply_discount(200, "gold")
    tax=calculate_tax(discounted, 0.07)
    after_tax=discounted + tax
    print(f"After gold discount : ${discounted:.2f}")
    print(f"After Tax: ${after_tax:.2f}")
      # refactor into a function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# exercise 4
orders=[(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total=final_price(price, tier, 0.07)
    print(f"Price: ${price}, Tier: {tier}, Final Price: ${total:.2f}")

    # exercise 6

    x=100

    def double_it():
        x=999
        return x * 2
print(x)
print(double_it())
print(x)  