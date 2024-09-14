class PresentationLayer:
    def __init__(self, business_layer):
        self.business_layer = business_layer

    def show_menu(self): # Menú principal
        print("Bienvenido a nuestra guardería de mascotas")
        while True: # Inicializar ciclo del menú
            print("\n1. Añadir cliente")
            print("2. Añadir servicio")
            print("3. Ver clientes")
            print("4. Ver servicios")
            print("5. Agendar servicio")
            print("6. Salir")

            choice = input("Elija una opción: ")

            # Llamar métodos que correspondan a las opciones
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.add_service()
            elif choice == "3":
                self.view_customers()
            elif choice == "4":
                self.view_services()
            elif choice == "5":
                self.book_service()
            elif choice == "6":
                print("Hasta pronto!")
                break # Romper el ciclo
            else:
                print("Opción errada, por favor ingrese una de las opciones del menú .") # Volver a intentar

    def add_customer(self):
        name = input("Ingrese el nombre del cliente: ") # Pedir nombre cliente
        pet_name = input("Ingrese el nombre de la mascota: ") # Pedir nombre mascota
        self.business_layer.add_customer(name, pet_name)
        print(f"{name} y {pet_name} han sido añadidos exitosamente.") # Regresar creación de cliente

    def add_service(self):
        service_name = input("Ingrese el nombre del servicio: ") # Pedir nombre servicio
        price = float(input("Ingrese el precio del servicio: ")) # Pedir precio servicio
        self.business_layer.add_service(service_name, price)
        print(f"{service_name} ha sido añadido como servicio.") # Regresar creacion de servicio

    def view_customers(self):
        customers = self.business_layer.get_customers() # Importar clientes mediante método de capa de negocio
        if customers:
            for customer in customers: # Atravesar lista customers
                print(f"Cliente: {customer['name']}, Mascota: {customer['pet_name']}") # Ver clientes y mascotas
        else:
            print("No hemos encontrado clientes.") # Notificar si todavía no hay clientes

    def view_services(self):
        services = self.business_layer.get_services() #Importar servicios mediantes método de capa de negocio
        if services:
            for service in services:
                print(f"Servicio: {service['service_name']}, Precio: ${service['price']}") # Ver servicios y precios
        else:
            print("No hemos encontrado servicios.") # Notificar si todavía no hay servicios

    def book_service(self):
        customer_name = input("Ingrese el nombre del cliente: ") # Pedir nombre del cliente
        service_name = input("Ingrese el nombre del servicio: ") # Pedir nombre del servicio
        result = self.business_layer.book_service(customer_name, service_name) # Verificar que existan el cliente y servicio mediante método de capa de negocio
        print(result) # Notificar sobre el agendamiento o el fallo
