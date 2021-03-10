# API

API Django Prueba

Antes de iniciar el proyecto configurar archivo .env dentro de la carpeta helpdesk, basándose en el archivo .env-sample

## Makefile commands

```bash
# install dependencies
make install

# seed users and tickets
make seeder

# migrate database
make migrations
```

## Seeded Users

Todos los usuarios tienen contraseña **12345678**
Nombres de usuario:
* __superuser__ (Superusuario)
* __viewuser__ (Solo puede ver tickets)
* __viewcreateuser__ (Ver y crear tickets)
