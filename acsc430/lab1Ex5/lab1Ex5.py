def main():
    food_charge = float(input("Enter the charge for the food: "))

    tip_rate = 0.10
    tax_rate = 0.05

    tip = food_charge * tip_rate
    tax = food_charge * tax_rate
    total = food_charge + tip + tax

    print(f"Food Charge: {food_charge:.2f}")
    print(f"Tip (10%): {tip:.2f}")
    print(f"Sales Tax (5%): {tax:.2f}")
    print(f"Total Amount: {total:.2f}")

main()