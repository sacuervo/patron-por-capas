class BusinessLayer:
    def __init__(self, data_layer):
        self.data_layer = data_layer # Iniciación instancia capa de datos

    def add_customer(self, name, pet_name):
        customer = { # Crear diccionario customer
            'name': name,
            'pet_name': pet_name
        }
        self.data_layer.add_customer(customer) # Guardar customer en capa de datos

    def add_service(self, service_name, price):
        service = { # Crear diccionario service
            'service_name': service_name,
            'price': price
        }
        self.data_layer.add_service(service) # Guardar service en capa de datos

    def get_customers(self):
        return self.data_layer.get_customers() # Ver lista customers mediante método de capa de datos

    def get_services(self):
        return self.data_layer.get_services() # Ver lista services mediante método de capa de datos

    def book_service(self, customer_name, service_name): # Agendar servicio
        customers = self.data_layer.get_customers() # Incializar referencia a customers de capa de datos
        services = self.data_layer.get_services() # Inicializer referencia a services de capa de datos

        customer = next((customer for customer in customers if c['name'] == customer_name), None) # Verificación de existencia del cliente
        service = next((service for service in services if s['service_name'] == service_name), None) # Verificación de existencia del servicio

        if customer and service: # Si ya se creó el cliente y el servicio...
            return f" Se ha agendado el servicio \"{service_name}\" para {customer['pet_name']}." # Agendamiento del servicio
        else:
                return "No se ha encontrado el cliente o el servicio indicado." # No se agenda el servicio
