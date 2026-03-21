# Steam Analytics Dashboard

Proyecto de análisis de datos de juegos de Steam usando Python, SQL Server, Streamlit y Flask.

---

## Descripción

Este proyecto permite analizar datos de juegos de Steam mediante un dashboard interactivo.

Incluye:

* Filtros por género, rating y precio
* Visualización de datos (Top 10 y promedios)
* Métricas clave (total de juegos, rating promedio, horas promedio)
* API para consultar los datos en formato JSON

---

## Tecnologías usadas

* Python
* SQL Server
* Streamlit
* Flask
* Pandas
* pyodbc

---

## Estructura del proyecto

```
steam-analytics-dashboard/
│
├── app.py
├── api.py
├── db.py
├── database.sql
├── steam_clean.csv
├── README.md
└── .gitignore
```

---

##  Instalación (PASO A PASO)

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/steam-analytics-dashboard.git
cd steam-analytics-dashboard
```

---

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
```

Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install streamlit pandas pyodbc flask requests
```

---

## Configurar base de datos (SQL Server)

### 1. Crear base de datos

En SQL Server ejecutar:

```sql
CREATE DATABASE steam_analytics;
```

---

### 2. Crear tabla

Ejecutar el archivo:

```
database.sql
```

---

### 3. Cargar datos

Usar el archivo:

```
steam_clean.csv
```

Puedes importarlo desde SQL Server Management Studio
o usar tu script de Python si ya lo tienes.

---

## Ejecutar el proyecto

### 🔹 Ejecutar Dashboard

```bash
python -m streamlit run app.py
```

Se abrirá automáticamente en el navegador.

---

### 🔹 Ejecutar API

```bash
python api.py
```

Luego abrir en navegador:

```
http://127.0.0.1:5000/games
```

Otros endpoints:

```
http://127.0.0.1:5000/top10
http://127.0.0.1:5000/metrics
```

---

## Prueba rápida de la API con Python

```python
import requests

data = requests.get("http://127.0.0.1:5000/games").json()

print(len(data))
print(data[0])
```

---

## Funcionalidades

* Visualización de datos en tabla
* Filtros interactivos
* Gráficos de análisis
* Métricas en tiempo real
* API REST para acceso a datos

---

## .gitignore recomendado

Crear archivo `.gitignore` con:

```
__pycache__/
venv/
steam.csv
games_api.csv
```

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de análisis de datos con Python y SQL Server.
