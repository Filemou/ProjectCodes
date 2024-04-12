import time
from collections import deque

class CheckoutLane:
    def __init__(self, lane_id, capacity):
        self.lane_id = lane_id
        self.status = 'closed'  # Lane starts as closed by default
        self.timestamp = time.time()  # Current time as the initial timestamp
        self.customers = deque()  # Customers will be managed in a queue
        self.capacity = capacity  # Maximum capacity of the lane

    def open_lane(self):
        self.status = 'open'
        self.timestamp = time.time()

    def close_lane(self):
        self.status = 'closed'
        self.timestamp = time.time()

    def add_customer(self, customer):
        # This method should be overridden in subclasses to handle different lane types
        raise NotImplementedError("This method should be implemented by subclasses.")

    def remove_customer(self):
        if self.customers:
            return self.customers.popleft()  # Remove a customer from the queue
        return None

    def display_lane_status(self):
        status = "Open" if self.status == 'open' else "Closed"
        customers_in_line = ''.join(['*' for _ in self.customers])  # Visual representation
        print(f"Lane {self.lane_id} [{status}] - Customers: {customers_in_line}")

class RegularLane(CheckoutLane):
    def __init__(self, lane_id):
        super().__init__(lane_id, capacity=5)  # Assuming a regular lane has a capacity of 5

    def add_customer(self, customer):
        if len(self.customers) < self.capacity:
            self.customers.append(customer)
        else:
            print("Lane is full. Customer cannot be added.")

class SelfServiceLane(CheckoutLane):
    def __init__(self, lane_id):
        super().__init__(lane_id, capacity=15)  # Assuming a self-service lane has a capacity of 8

    def add_customer(self, customer):
        if len(self.customers) < self.capacity:
            self.customers.append(customer)
        else:
            print("Lane is full. Customer cannot be added.")

# Example usage
regular_lane = RegularLane(1)
self_service_lane = SelfServiceLane(2)

regular_lane.open_lane()
self_service_lane.open_lane()

# Assuming customer is an object of Customer class with required attributes
# Add a customer to a lane based on their basket size (pseudo code)
# if customer.items_in_basket < 10:
#     self_service_lane.add_customer(customer)
# else:
#     regular_lane.add_customer(customer)

regular_lane.display_lane_status()
self_service_lane.display_lane_status()

# After some processing, remove a customer
regular_lane.remove_customer()
self_service_lane.remove_customer()

regular_lane.display_lane_status()
self_service_lane.display_lane_status()
