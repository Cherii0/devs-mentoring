

class Manager:

    def __init__(self):
        self.__orders = {}

    def add_order(self, order):

        if len(self.__orders) == 0:
            self.__orders[order] = 1
            return

        for key in self.__orders.keys():
            if order.get_order_id() == key.get_order_id():
                self.__orders[key] += 1
                return

        self.__orders[order] = 1

    def remove_order(self, order_id):

        for order in self.__orders.keys():
            if order.get_order_id() == order_id:
                if self.__orders[order] == 1:
                    del self.__orders[order]
                    return
                else:
                    self.__orders[order] -= 1
                    return

        print(f"there is no order with id {order_id}")

    def describe_orders(self):
        print(self.__orders)

class Order:

    def __init__(self, order_id = 0, order_name = "order", price = 0):
        self.__order_id = order_id
        self.__order_name = order_name
        self.__price = price

    def get_order_id(self):
        return self.__order_id


def main():
    manager = Manager()

    # orders dict before adding orders
    manager.describe_orders()

    # adding some orders
    manager.add_order(Order(order_id = 251, order_name = "order", price = 2500))
    manager.add_order(Order(order_id = 251, order_name = "order", price = 2500))
    manager.add_order(Order(order_id = 251, order_name = "order", price = 2500))
    manager.add_order(Order(order_id = 221, order_name = "order", price = 1500))
    manager.add_order(Order(order_id = 251, order_name = "order", price = 1500))
    manager.add_order(Order(order_id = 111, order_name = "order", price = 1500))

    # orders after adding and before removing
    manager.describe_orders()

    # removing some orders
    manager.remove_order(order_id = 251)
    manager.remove_order(order_id = 111)

    # orders after removing some orders
    manager.describe_orders()


if __name__ == "__main__":
    main()
