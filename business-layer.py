class BusinessLayer:
    def __init__(self, data_layer):
        self.data_layer = data_layer

    def add_customer(self, name, pet_name):
        customer = {
            'name': name,
            'pet_name': pet_name
        }
        self.data_layer.add_customer(customer)

    def add_service(self, service_name, price):
        service = {
            'service_name': service_name,
            'price': price
        }
        self.data_layer.add_service(service)

    def get_customers(self):
        return self.data_layer.get_customers()

    def get_services(self):
        return self.data_layer.get_services()

    def book_service(self, customer_name, service_name):
        customers = self.data_layer.get_customers()
        services = self.data_layer.get_services()

        customer = next((c for c in customers if c['name'] == customer_name), None)
        service = next((s for s in services if s['service_name'] == service_name), None)

        if customer and service:
            return f"{customer['pet_name']} has been booked for {service_name} service."
        else:
            return "Customer or service not found."
