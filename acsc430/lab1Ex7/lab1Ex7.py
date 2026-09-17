def main():
    shares = 1000
    buy_price = 32.87
    sell_price = 33.92
    commission_rate = 0.02

    amount_paid = shares * buy_price
    buy_commission = amount_paid * commission_rate

    amount_sold = shares * sell_price
    sell_commission = amount_sold * commission_rate

    final_amount = amount_sold - sell_commission - amount_paid - buy_commission

    print(f"Amount Paid for Stock: {amount_paid:.2f}")
    print(f"Commission Paid (Buy): {buy_commission:.2f}")
    print(f"Amount Sold For: {amount_sold:.2f}")
    print(f"Commission Paid (Sell): {sell_commission:.2f}")

    if final_amount > 0:
        print(f"Profit: {final_amount:.2f}")
    else:
        print(f"Loss: {abs(final_amount):.2f}")

main()