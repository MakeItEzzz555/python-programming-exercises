

import csv

from Product import Books, Electronics, TVs


FIELDNAMES = [
    "SerialNumber",
    "Product_Type",
    "Title",
    "Manufacturer/Author",
    "Year Published",
    "regularPrice",
    "Discount",
    "Size",
    "SmartTv",
]


def parse_bool(value):
    return str(value).strip().upper() in ("TRUE", "YES", "Y", "1")


def input_required(prompt):
    value = input(prompt).strip()
    while value == "":
        print("This value is required.")
        value = input(prompt).strip()
    return value


def input_float(prompt):
    while True:
        try:
            return float(input_required(prompt))
        except ValueError:
            print("Please enter a valid number.")


def input_int(prompt):
    while True:
        try:
            return int(input_required(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def input_bool(prompt):
    while True:
        value = input_required(prompt + " (True/False): ")
        if value.strip().upper() in ("TRUE", "YES", "Y", "1"):
            return True
        if value.strip().upper() in ("FALSE", "NO", "N", "0"):
            return False
        print("Please enter True or False.")


def input_optional(prompt, current_value):
    value = input(f"{prompt} [{current_value}]: ").strip()
    if value == "":
        return current_value
    return value


def create_product(row):
    product_type = row["Product_Type"].strip().lower()
    serial = row["SerialNumber"]
    title = row["Title"]
    creator = row["Manufacturer/Author"]
    price = row["regularPrice"]
    discount = row["Discount"]

    if product_type == "electronics":
        return Electronics(serial, title, price, creator, discount)

    if product_type == "tv":
        return TVs(
            serial,
            title,
            price,
            creator,
            row.get("Size", 0),
            parse_bool(row.get("SmartTv", False)),
            discount,
        )

    if product_type == "book":
        return Books(serial, title, price, creator, row.get("Year Published", 0), discount)

    raise ValueError(f"Unknown product type: {row['Product_Type']}")


def product_to_row(product):
    row = dict.fromkeys(FIELDNAMES, "")
    row["SerialNumber"] = product.getSerialNumber()
    row["Title"] = product.getTitle()
    row["regularPrice"] = product.getRegularPrice()

    if isinstance(product, TVs):
        row["Product_Type"] = "TV"
        row["Manufacturer/Author"] = product.getManufacturer()
        row["Discount"] = product.getDiscount()
        row["Size"] = product.getSize()
        row["SmartTv"] = str(product.getSmartTv()).upper()
    elif isinstance(product, Electronics):
        row["Product_Type"] = "Electronics"
        row["Manufacturer/Author"] = product.getManufacturer()
        row["Discount"] = product.getDiscount()
    elif isinstance(product, Books):
        row["Product_Type"] = "Book"
        row["Manufacturer/Author"] = product.getAuthor()
        row["Year Published"] = product.getYear()
        row["Discount"] = product.getDiscount()

    return row


def load_products(products):
    filename = input_required("Enter CSV filename to load: ")
    count = 0

    try:
        with open(filename, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not row.get("SerialNumber"):
                    continue
                products.append(create_product(row))
                count += 1
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    except (KeyError, ValueError) as error:
        print(f"Could not load product data: {error}")
        return

    print(f"{count} products were added")


def list_products(products):
    if not products:
        print("No products available.")
        return

    for product in products:
        print(product)


def list_electronics(products):
    found = False
    for product in products:
        if isinstance(product, Electronics):
            print(product)
            found = True

    if not found:
        print("No electronic products available.")


def list_non_electronics(products):
    found = False
    for product in products:
        if not isinstance(product, Electronics):
            print(product)
            found = True

    if not found:
        print("No non-electronic products available.")


def add_electronic(products):
    serial = input_int("Serial number: ")
    title = input_required("Title: ")
    manufacturer = input_required("Manufacturer: ")
    price = input_float("Regular price: ")
    discount = input_float("Discount (0.1 for 10% or 10 for 10%): ")
    products.append(Electronics(serial, title, price, manufacturer, discount))
    print("Electronic product added.")


def add_tv(products):
    serial = input_int("Serial number: ")
    title = input_required("Title: ")
    manufacturer = input_required("Manufacturer: ")
    price = input_float("Regular price: ")
    discount = input_float("Discount (0.1 for 10% or 10 for 10%): ")
    size = input_int("Size in inches: ")
    smart = input_bool("Smart TV")
    products.append(TVs(serial, title, price, manufacturer, size, smart, discount))
    print("TV product added.")


def add_book(products):
    serial = input_int("Serial number: ")
    title = input_required("Title: ")
    author = input_required("Author: ")
    year = input_int("Year published: ")
    price = input_float("Regular price: ")
    discount = input_float("Discount (0.1 for 10% or 10 for 10%): ")
    products.append(Books(serial, title, price, author, year, discount))
    print("Book added.")


def find_product(products, serial):
    for product in products:
        if product.getSerialNumber() == serial:
            return product
    return None


def edit_product(products):
    serial = input_int("Enter serial number to edit: ")
    product = find_product(products, serial)

    if product is None:
        print("Product not found.")
        return

    print(f"Editing: {product}")
    product.setTitle(input_optional("Title", product.getTitle()))
    product.setRegularPrice(input_optional("Regular price", product.getRegularPrice()))

    if isinstance(product, Electronics):
        product.setManufacturer(input_optional("Manufacturer", product.getManufacturer()))
        product.setDiscount(input_optional("Discount", product.getDiscount()))

    if isinstance(product, TVs):
        product.setSize(input_optional("Size", product.getSize()))
        product.setSmartTv(parse_bool(input_optional("SmartTV", product.getSmartTv())))

    if isinstance(product, Books):
        product.setAuthor(input_optional("Author", product.getAuthor()))
        product.setYear(input_optional("Year published", product.getYear()))
        product.setDiscount(input_optional("Discount", product.getDiscount()))

    print("Product updated.")


def store_products(products):
    filename = input_required("Enter CSV filename to store: ")

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for product in products:
            writer.writerow(product_to_row(product))

    print(f"{len(products)} Products written to file")


def print_menu():
    print()
    print("a) Load product data from CSV")
    print("b) List ALL products")
    print("c) List Electronic products")
    print("d) List non-Electronic products")
    print("e) Add Electronic product")
    print("f) Add a TV product")
    print("g) Add a Book")
    print("h) Edit product")
    print("i) Store product data in CSV")
    print("q) Quit")


def main():
    products = []

    while True:
        print_menu()
        choice = input("Enter choice: ").strip().lower()

        if choice == "a":
            load_products(products)
        elif choice == "b":
            list_products(products)
        elif choice == "c":
            list_electronics(products)
        elif choice == "d":
            list_non_electronics(products)
        elif choice == "e":
            add_electronic(products)
        elif choice == "f":
            add_tv(products)
        elif choice == "g":
            add_book(products)
        elif choice == "h":
            edit_product(products)
        elif choice == "i":
            store_products(products)
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
