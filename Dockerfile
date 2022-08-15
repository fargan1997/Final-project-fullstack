# obtener imagen de base
FROM python:3.9.7

#Establecer variables de entorno 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Configurar diretorio d etrabajo 
WORKDIR /code

# Instalar dependencias
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copiar proyecto
COPY . /code/