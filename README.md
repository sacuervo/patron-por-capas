# Patrón por capas - Guardería de mascotas

## Objetivo
- Explicar el patrón de diseño por capas mediante un sistema de información para una guardería de mascotas.

## data-layer.py
- Contiene la implementación de la capa de datos de la aplicación

### Constructor
- Inicializa instancias con listas `customer` y `services` para contener a los clientes y servicios de la guardería respectivamente

### `add_customer()` y `add_service()`
- Permite añadir clientes a lista `customer` y servicios a lista `services`
- Reciben como argumentos un diccionario de usuario y servicio respectivamente

### `get_customers()` y `get_services()`
- Permite visualizar elementos de lista `customer` y elementos de lista `services`

## `business-layer.py`

### Constructor
- Inicializa instancias con la declaración de una instancia de la capa de datos para trabajar

### `add_customer()`
- Recibe diccionario con el nombre del usuario y de su mascota e invoca método de capa de datos para creación del usuario
 
### `add_service()`
- Recibe nombre del servicio y precio e invoca método de capa de datos para la creación del servicio 

### `get_customers()`
- Regresa la lista de diccionarios de clientes mediante método de capa de datos

### `get_services()`
- Regresa la lista de diccionarios de servicios mediante método de capa de datos

### `book_services()`
- Permite agendar servicios
- Recibe nombre del cliente y del servicio a prestar para la verificación de su existencia
