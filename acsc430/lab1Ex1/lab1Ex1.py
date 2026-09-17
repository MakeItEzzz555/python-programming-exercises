
def calc_discount(item_price):
        discount = item_price * 0.20
        return discount
def calc_price(item_price, discount):
    price = item_price - discount
    return price
def main():
    item_price = float(input("Enter your item price: "))
    discount = calc_discount(item_price)
    price = calc_price(item_price, discount)
    print("Your item price is $" + str(price))

main()