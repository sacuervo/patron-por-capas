# data_layer.py

class DataLayer:
    def __init__(self):
        self.customers = [] # Lista que contiene los clientes en forma de diccionarios
        self.services = [] # Lista que contiene los servicios en forma de diccionarios

    def add_customer(self, customer): # Añadir cliente a lista
        self.customers.append(customer)

    def add_service(self, service): # Añadir servicio a lista
        self.services.append(service)

    def get_customers(self): # Ver lista clientes. Requiere ser accedido por business_layer.py, por lo tanto no es privado
        return self.customers

    def get_services(self): # Ver lista servicios. Requiere ser accedido por business_layer.py, por lo tanto no es privado
        return self.services
