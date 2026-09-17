def sale_sum(items):
    total = 0
    for item in items:
        total += item
    return total

def sale_tax(items, tax):
    return sale_sum(items) * tax

def sale_total(items, tax):
    return sale_sum(items) + sale_tax(items, tax)

def get_items(items):
    for i in range(5):
        item = float(input("Enter item " + str(i + 1) + ": "))
        items.append(item)
    return items

def print_all(items, tax):
    subtotal = sale_sum(items)
    tax_amount = sale_tax(items, tax)
    total = sale_total(items, tax)

    print("Subtotal of Sale: " + str(subtotal))
    print("Sale Tax: " + str(tax_amount))
    print("Total Sale: " + str(total))

def main():
    tax = 0.19
    items = []
    get_items(items)
    print_all(items, tax)

main()