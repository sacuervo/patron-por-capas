# Patrón por capas - Guardería de mascotas

## Objetivo
- Explicar el patrón de diseño por capas mediante un sistema de información para una guardería de mascotas.

## data-layer.py
- Contiene la implementación de la capa de datos de la aplicación

### Constructor
- Inicializa instancias con listas `customer` y `services` para contener a los clientes y servicios de la guardería respectivamente

### `add_customer()` y `add_service()`
- Permite añadir clientes a lista `customer` y servicios a lista `services`

### `get_customers()` y `get_services()`
- Permite visualizar elementos de lista `customer` y elementos de lista `services`