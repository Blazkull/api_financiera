# API Financiera

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Warp](https://img.shields.io/badge/Warp-Terminal-black.svg)](https://warp.dev/)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-IDE-blue.svg)](https://code.visualstudio.com/)
[![Postman](https://img.shields.io/badge/Postman-API%20Client-orange.svg)](https://www.postman.com/)

Esta es una API REST diseñada para gestionar información financiera de manera eficiente, cubriendo usuarios, ingresos, gastos y proporcionando un panel de control analítico.

## Descripción

La API ofrece endpoints para realizar las siguientes operaciones:

- **Usuarios:** Gestión completa de usuarios (crear, obtener, actualizar, eliminar).
- **Ingresos:** Registro y gestión de ingresos (crear, obtener, actualizar, eliminar).
- **Gastos:** Registro y gestión de gastos (crear, obtener, actualizar, eliminar).
- **Dashboard:** Visualización de información financiera resumida y análisis.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **FastAPI:** Framework web moderno y de alto rendimiento para APIs.
- **PyMySQL:** Conector de base de datos para MySQL.
- **MySQL Workbench:** Herramienta de administración y modelado de base de datos.
- **Postman:** Herramienta para pruebas y documentación de la API.
- **Warp:** Terminal utilizado para el desarrollo.

## Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Warp (última versión, opcional)
- Postman (opcional)

Si deseas probar localmente, debes crear una base de datos con los parámetros que se encuentran en el archivo [`bd.txt`](https://github.com/Blazkull/api_financiera/blob/main/bd.txt) dentro del repositorio.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Blazkull/api_financiera.git
   cd api_financiera
   ```

2. Crear un entorno virtual (recomendado):

   ```bash
   python -m venv .\local
   source local/bin/activate # Para macOS y Linux
   local\Scripts\activate # Para Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

La API utiliza MySQL Workbench como base de datos. Para configurarla, modifica la URL de conexión en `database.py`.

Si deseas probar localmente, debes crear una base de datos con los parámetros indicados en el archivo [`bd.txt`](https://github.com/Blazkull/api_financiera/blob/main/bd.txt), que contiene la configuración necesaria para establecer la conexión.

## Ejecución

La API se prueba mediante **Postman**, utilizando los métodos HTTP correspondientes para interactuar con los endpoints.

## Endpoints

### Usuarios

- **POST** `/api/usuarios/`: Crea un nuevo usuario.
- **GET** `/api/usuarios/{usuario_id}`: Obtiene un usuario por ID.
- **PUT** `/api/usuarios/{usuario_id}`: Actualiza un usuario existente.
- **DELETE** `/api/usuarios/{usuario_id}`: Elimina un usuario.

### Ingresos

- **POST** `/api/ingresos/`: Crea un nuevo ingreso.
- **GET** `/api/ingresos/{ingreso_id}`: Obtiene un ingreso por ID.
- **PUT** `/api/ingresos/{ingreso_id}`: Actualiza un ingreso existente.
- **DELETE** `/api/ingresos/{ingreso_id}`: Elimina un ingreso.

### Gastos

- **POST** `/api/gastos/`: Crea un nuevo gasto.
- **GET** `/api/gastos/{gasto_id}`: Obtiene un gasto por ID.
- **PUT** `/api/gastos/{gasto_id}`: Actualiza un gasto existente.
- **DELETE** `/api/gastos/{gasto_id}`: Elimina un gasto.

### Dashboard

- **GET** `/api/dashboard/`: Obtiene información del dashboard.

## Integrantes del Proyecto

- **Jhoan Acosta:** [https://github.com/Blazkull](https://github.com/Blazkull)
- **Kevin Pérez:** [https://github.com/kevperez](https://github.com/kevperez)
- **Rafael Jimenez:** [https://github.com/rafaeljimenezc](https://github.com/rafaeljimenezc)

## Contribución

1. Haz un fork del repositorio.
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -am 'Añade nueva característica'`).
4. Sube al branch (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT.

## Contacto

Si tienes preguntas o comentarios, no dudes en contactarme.

