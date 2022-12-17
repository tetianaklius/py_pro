class Product:
    def __init__(self, name: str, price: float):
        if price <= 0:
            raise ValueError("The price can`t be zero or a negative number")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"
