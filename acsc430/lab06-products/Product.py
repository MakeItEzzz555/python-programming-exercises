# Lab 6 - Classes and Object-Oriented Programming
# Classes for Product, Electronics, Books, and TVs.


def normalize_discount(discount):
    value = float(discount or 0)
    if value > 1:
        value = value / 100
    return value


def format_discount(discount):
    return f"{normalize_discount(discount) * 100:g}%"


def normalize_bool(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().upper() in ("TRUE", "YES", "Y", "1")


class Product:
    def __init__(self, serialNumber, title, regularPrice):
        self.serialNumber = int(serialNumber)
        self.title = title
        self.regularPrice = float(regularPrice)

    def setRegularPrice(self, regularPrice):
        self.regularPrice = float(regularPrice)

    def getRegularPrice(self):
        return self.regularPrice

    def setSerialNumber(self, sn):
        self.serialNumber = int(sn)

    def getSerialNumber(self):
        return self.serialNumber

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def __str__(self):
        return f"{self.serialNumber}, Product, {self.title}, €{self.regularPrice}"


class Electronics(Product):
    def __init__(self, serialNumber, title, regularPrice, manufacturer="", discount=0):
        super().__init__(serialNumber, title, regularPrice)
        self.manufacturer = manufacturer
        self.discount = normalize_discount(discount)

    def setManufacturer(self, mfct):
        self.manufacturer = mfct

    def getManufacturer(self):
        return self.manufacturer

    def setDiscount(self, discount):
        self.discount = normalize_discount(discount)

    def getDiscount(self):
        return self.discount

    def computeDiscount(self, regularPrice=None, discount=None):
        price = self.regularPrice if regularPrice is None else float(regularPrice)
        disc = self.discount if discount is None else normalize_discount(discount)
        return price - (price * disc)

    def __str__(self):
        return (
            f"{self.serialNumber}, Electronics, {self.title}, {self.manufacturer}, "
            f"€{self.regularPrice}, Discount: {format_discount(self.discount)}"
        )


class Books(Product):
    def __init__(self, serialNumber, title, regularPrice, author="", yearPublished=0, discount=0):
        super().__init__(serialNumber, title, regularPrice)
        self.author = author
        self.yearPublished = int(yearPublished or 0)
        self.discount = normalize_discount(discount)

    def setAuthor(self, Author):
        self.author = Author

    def getAuthor(self):
        return self.author

    def setYear(self, Year):
        self.yearPublished = int(Year)

    def getYear(self):
        return self.yearPublished

    def setDiscount(self, discount):
        self.discount = normalize_discount(discount)

    def getDiscount(self):
        return self.discount

    def computeDiscount(self, regularPrice=None, discount=None):
        price = self.regularPrice if regularPrice is None else float(regularPrice)
        disc = self.discount if discount is None else normalize_discount(discount)
        return price - (price * disc)

    def __str__(self):
        return (
            f"{self.serialNumber}, Book, {self.title}, {self.author}, "
            f"Year Published: {self.yearPublished}, €{self.regularPrice}, "
            f"Discount: {format_discount(self.discount)}"
        )


class TVs(Electronics):
    def __init__(
        self,
        serialNumber,
        title,
        regularPrice,
        manufacturer="",
        size=0,
        smartTV=False,
        discount=0,
    ):
        super().__init__(serialNumber, title, regularPrice, manufacturer, discount)
        self.size = int(size or 0)
        self.smartTV = normalize_bool(smartTV)

    def setSize(self, size):
        self.size = int(size)

    def getSize(self):
        return self.size

    def setSmartTv(self, smart):
        self.smartTV = normalize_bool(smart)

    def getSmartTv(self):
        return self.smartTV

    def computeDiscount(self, regularPrice=None, discount=None):
        return super().computeDiscount(regularPrice, discount)

    def __str__(self):
        return (
            f"{self.serialNumber}, TV, {self.title}, {self.manufacturer}, "
            f"€{self.regularPrice}, Discount: {format_discount(self.discount)}, "
            f"Size: {self.size} inches, SmartTV: {self.smartTV}"
        )
