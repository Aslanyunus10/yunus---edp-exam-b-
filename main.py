class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class OrderSubmittedEvent(Event):
    def __init__(self, order_id, customer_id):
        super().__init__("OrderSubmitted", {"order_id": order_id, "customer_id": customer_id})

class OrderRejectedEvent(Event):
    def __init__(self, order_id, reason):
        super().__init__("Order_rejected", {"Order_id:",order_id "reason": reason}

class CommunicationQueue:
     def __init__(self):
        self.queue = []
     
     def add_event(self, name):
        print(f"Event added: {event.name}")
        self.queue.append(event)

    def process_event(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {event.name}, Payload: {event.payload}")

class Store:
    def __init__(self, queue):
        self.queue = queue

    def submit_order(self, order_id, customer_id):
        print(f"Submitting order: {order_id} for customer {customer_id}")
        event = OrderSubmittedEvent(order_id, customer_id)
        self.queue.add_event(event)

    def reject_order(self, order_id, reason):
        print(f"Rejecting order: {order_id}, Reason: {reason}")
        event = OrderRejectedEvent(order_id, reason)
        self.queue.add_event(event)

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
    
    def place_order(self, store, order_id):
        print(f"{self.name} is placing an order: {order_id}")
        store.submit_order(order_id, self.customer_id)

if __name__ == "__main__":
    queue = CommunicationQueue()
    store = Store(queue)

    customer1 = Customer(1, "Messi")
    customer2 = Customer(2, "Ronaldo")

    customer1.place_order(store, "Warsaw")
    customer2.place_order(store, "Ankara")

    store.reject_order("Warsaw", "No stock")




