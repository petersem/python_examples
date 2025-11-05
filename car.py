from enum import Enum

# extra percentage cost for some colors
class ColorPercent(Enum):
    RED = 5
    GREEN = 2
    BLUE = 3
    WHITE = 0
    GREY = 0
    GREY_METALIC = 7

# define the costs for each model type
class Model(Enum):
    BASE = 0
    SPORT = 2000
    LUXUARY = 5000

class Car:
    def __init__(self, color_percent, model):
        self.color_percent = color_percent
        self.vehicle_model = model
        self.base_cost = 20000

    def adjusted_cost(self):
        return self.base_cost + (self.base_cost * self.color_percent.value / 100) + self.vehicle_model.value

class Orders:
    def __init__(self,sale_tax):
        self.orders = []
        self.sales_tax = sale_tax

    def add(self, car):
        self.orders.append(car)

    def discounted(self):
        if self.quantity > 2:
            return True
        else:
            return False

    @property
    def quantity(self):
        return len(self.orders)

    @property
    def total_pretax_cost(self):
        total_cost = 0
        for ac in self.orders:
            total_cost += ac.adjusted_cost()

        if self.quantity > 2:
            total_cost = total_cost - (total_cost * 5 / 100)

        return total_cost

    @property
    def sales_tax_amount(self):
        return self.total_pretax_cost * (self.sales_tax/100)

    @property
    def total_cost(self):
        # sales tax must be applied to final cost after all additions and discounts
        total = self.total_pretax_cost + self.sales_tax_amount
        return total

    def order_details(self):
        details = "\r\n"
        for o in self.orders:
            details = details + o.color_percent.name + ' - ' + o.vehicle_model.name + '\r\n'

        return details

# define orders object and sales tax
my_orders = Orders(5) # set to 5% sales tax

# add car objects to orders
my_orders.add(Car(ColorPercent.WHITE, Model.BASE))
my_orders.add(Car(ColorPercent.GREY_METALIC, Model.SPORT))
my_orders.add(Car(ColorPercent.RED, Model.LUXUARY))

print("Ordered cars:",my_orders.quantity)
print("3 or more discount applied:",my_orders.discounted())
print("Sales tax %:",my_orders.sales_tax)
print("Total sales tax $:",my_orders.sales_tax_amount)
print("Total pre-tax cost $:",my_orders.total_pretax_cost)
print("Total cost $:",my_orders.total_cost)
print("Details:", my_orders.order_details())

