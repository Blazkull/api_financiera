# API Financiera

Esta es una API REST para gestionar información financiera, incluyendo usuarios, cuentas, transacciones y tipos de transacción.

## Descripción

La API proporciona endpoints para realizar las siguientes operaciones:

* **Usuarios:** Crear, obtener, actualizar y eliminar usuarios.


## Tecnologías Utilizadas

* **Python:** Lenguaje de programación principal.
* **Flask:**
* **PyMySQL:**

## Requisitos

* Python 3.7 o superior
* Pip (gestor de paquetes de Python)

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/Blazkull/api\_financiera.git](https://github.com/Blazkull/api_financiera.git)
    cd api_financiera
    ```

2.  Crea un entorno virtual (recomendado):

    ```bash
    python -m venv .\local
    local\\Scripts\\activate
    ```

3.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
     ```

## Configuración

La API utiliza una base de datos SQLite por defecto. Si deseas utilizar otra base de datos, puedes modificar la URL de la base de datos en el archivo `database.py`.

## Ejecución

Para ejecutar la API, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
 ```

La API estará disponible en `http://127.0.0.1:8000`.

## Documentación

La documentación de la API se genera automáticamente utilizando Swagger UI y Redoc. Puedes acceder a ella en las siguientes URLs:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **Redoc:** `http://127.0.0.1:8000/redoc`

## Endpoints

A continuación, se describen algunos de los endpoints principales de la API:

### Usuarios

* `POST /users/`: Crea un nuevo usuario.
* `GET /users/{user_id}`: Obtiene un usuario por su ID.
* `PUT /users/{user_id}`: Actualiza un usuario existente.
* `DELETE /users/{user_id}`: Elimina un usuario.

### Ingresos

* `POST /ingresos/`: Crea una nueva cuenta bancaria.
* `GET /ingresos/{ingresos_id}`: Obtiene una cuenta por su ID.
* `PUT /ingresos/{ingresos_id}`: Actualiza una cuenta existente.
* `DELETE /ingresos/{ingresos_id}`: Elimina una cuenta.

### GASTOS


### Dashboard


## Integrantes del Proyecto

* **Jhoan Acosta:** [https://github.com/anagarcia-dev](https://github.com/anagarcia-dev)
* **Kevin Pérez:** [https://github.com/carlosperez-code](https://github.com/carlosperez-code)
* **Rafael Jimenez:** [https://github.com/laurarodriguez-tech](https://github.com/laurarodriguez-tech)

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1.  Haz un fork del repositorio.
2.  Crea una rama con tu nueva característica o corrección de errores.
3.  Realiza tus cambios y commitea tus cambios.
4.  Envía un pull request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT.

## Contacto

Si tienes alguna pregunta o comentario, no dudes en contactarme.
