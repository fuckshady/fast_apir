# Imagen base de Python
FROM python:3.13.3-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la carpeta app al contenedor
COPY ./app ./app

# Comando para arrancar el servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
