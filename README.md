# Inventory API

## Setup

# Inventory API

## Descripción del Proyecto

Esta es una API RESTful para gestionar el inventario de una tienda de abarrotes. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los artículos del inventario. La API utiliza autenticación básica para proteger los endpoints.

## Instalación y Configuración

1. **Clona el repositorio:**
    ```bash
    git clone <repository-url>
    ```

2. **Navega al directorio del proyecto:**
    ```bash
    cd inventory_api
    ```

3. **Crea un entorno virtual:**
    ```bash
    python -m venv venv
    ```

4. **Activa el entorno virtual:**

    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```

    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Instala los paquetes requeridos:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución del Servidor

Para ejecutar el servidor, usa el siguiente comando:
```bash
python app.py


## Endpoints

- `GET /items`: List all items.
- `POST /item/<item_id>`: Create a new item.
- `GET /item/<item_id>`: Get item details.
- `PUT /item/<item_id>`: Update an item.
- `DELETE /item/<item_id>`: Delete an item.
