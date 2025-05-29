
class OrderManager:

    def __init__(self, orders):
        self.orders = orders
        self.orders_ids, self.orders_pricing_pre_adjust = [], []
        self.orders_pricing, self.invoice = [], []
        self.approach = 1

    def create_invoice_1(self):
        # approach 1
        self.approach = 1
        self.orders_ids = list(map(lambda order : order[0], self.orders))
        self.orders_pricing_pre_adjust = list(map(lambda order : order[-1] * order[-2] , self.orders))
        self.orders_pricing = list(map(lambda order : order+10 if order < 100 else order, self.orders_pricing_pre_adjust))
        self.invoice = list(map(lambda order_id, order_pricing : (order_id, order_pricing), self.orders_ids, self.orders_pricing))


    def create_invoice_2(self):
        # approach 2
        self.approach = 2
        self.invoice = list(map(lambda order : (order[0], order[-1] * order[-2]) if (order[-1] * order[-2]) >= 100 else  (order[0], order[-1] * order[-2] + 10), self.orders))

    def show_invoice(self):
        print(f"approach {self.approach} invoice : ")
        print(self.invoice)

def main():
    orders = [
        ["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
            ]
    orders_manager = OrderManager(orders)
        # approach 1
    orders_manager.create_invoice_1()
    orders_manager.show_invoice()
        # approach 2
    orders_manager.create_invoice_2()
    orders_manager.show_invoice()

if __name__ == "__main__":
    main()
