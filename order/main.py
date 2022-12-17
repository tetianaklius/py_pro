import product_
import order_
import customer_

if __name__ == "__main__":
    try:
        milk = product_.Product("milk", 25)
        grapefruit = product_.Product("grapefruit", 75.25)
        chocolate = product_.Product("chocolate", 45)
        customer = customer_.Customer("Andrii", "35", "380_66_451_5878", "Lviv")

        print(grapefruit)
        print(customer)
        print("----------------------------")

        order = order_.Order(customer)

        order.add_product(milk, 1)
        order.add_product(grapefruit, 3)
        order.add_product(chocolate, 2)

        print(order)

    except Exception as error:
        print(error)
