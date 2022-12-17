import customer_
import product_


class Order:
    def __init__(self, customer: customer_.Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: product_.Product, quantity: float = 1):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total_cost(self):
        suma = 0
        for index, item in enumerate(self.products):
            suma += item.price * self.quantities[index]
        return suma

    def __str__(self):
        res = '\n'.join(map
                (lambda item: f"{item[0]} × {item[1]} = {item[0].price * item[1]} UAH",
                zip(self.products, self.quantities))
                )
        return f"{self.customer}\n-order-\n{res}\nTotal: {self.total_cost()} UAH"
