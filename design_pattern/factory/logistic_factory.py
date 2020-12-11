from abc import ABC

class Logistics(ABC):

    def __init__(self):
        self.product = self.factory_method()

    def factory_method(self):
        pass

    def run_delivery(self):
        print("Running some complex operations")        
        self.product.deliver()

class RoadLogistics(Logistics):

    def factory_method(self):
        return Truck()

class SeaLogistics(Logistics):

    def factory_method(self):
        return Ship()

class Transport(ABC):

	def deliver(self):
    	pass

class Truck(Transport):

    def deliver(self):
    	print("truck delivering stuff")

class Ship(Transport):

    def deliver(self):
        print("ship delivering stuff")


if __name__ == "__main__":
    logistics = RoadLogistics()
    logistics.run_delivery()