# Conexión con Firebase DB

## Descripción

Programa para obtener los precios de los artículos de una base de datos en Firebase, y actualizarlos basados en la URL de localización original del producto (inicialmente solo válido para Amazon)

## Instalación

- Descargar Python 3 (Desarrollado y probado con Python v3.7.6)
- Abrir esta carpeta en una consola de Windows y ejecutar:

```
>> python -m venv env
>> env\Scripts\activate.bat
>> pip install -r requirements.txt
```

## Ejecución

Después de instalar y configurar el proyecto, correr los siguientes comandos para ejecutar la aplicación.

```
>> python main.py
```

## Manual de Usuario



___

## Dev info

Para conectar a la base de datos. En Firebase ir a *Project Settings > Service Accounts > Generate Private Key*, almacenar el .json en la carpeta `db_key/`

La estructura de la base de datos en Firebase es `{collections, documents, fields}`, que asemeja la estructura `{tables, registries, fields}` de una base de datos relacional.

En Amazon, crear una cuanta en [Amazon Web Services](https://aws.amazon.com/). Luego ir al `Perfil > My Security Credentials > Access keys > Create New Access Key > Download`, colocar el archivo en la carpeta `db_key/`.

AWS packages: https://github.com/yoavaviram/python-amazon-simple-product-api