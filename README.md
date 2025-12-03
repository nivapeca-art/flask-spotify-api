# Proyecto Flask + Spotipy

API para manejar usuarios y preferencias musicales usando Spotify.

Este proyecto permite:

- Crear, actualizar y eliminar usuarios.
- Agregar y consultar preferencias musicales de cada usuario.
- Consultar información de artistas en Spotify (géneros, canciones populares).

## Instalación
1. Clonar el repo

git clone https://github.com/nivapeca-art/flask-spotify-api.git
cd flask-spotify-api

2. Crear un `.env` con tus credenciales de Spotify

CLIENT_ID=tu_client_id_aqui
CLIENT_SECRET=tu_client_secret_aqui

3. Instalar dependencias: `pip install -r requirements.txt`

4. Correr: `python spotify_api.py`

## Endpoints

1. Usuarios
- POST /usuarios → Crear un usuario con nombre y edad.
JSON { "nombre": "Nicolle", "edad": 23 }
    Respuesta
    { "id": 1, "nombre": "Nicolle", "edad": 23 }

- GET /usuarios → Listar todos los usuarios.
    Respuesta
    [{"id":1,"nombre":"Nicolle","edad":23}]

- GET /usuarios/<id> → Obtener un usuario específico.
    Respuesta
    { "id": 1, "nombre": "Nicolle", "edad": 23 }

- PUT /usuarios/<id> → Actualizar datos de un usuario.
{ "id": 1, "nombre": "Nicolle", "edad": 23 }
    Respuesta
    { "nombre": "Nicolle Perez" }

- DELETE /usuarios/<id> → Eliminar un usuario.
    Respuesta
    { "mensaje": "Usuario eliminado" }


2. Preferencias musicales

- POST /usuarios/<id>/preferencias → Agregar un artista a las preferencias del usuario.
JSON { "artista": "Ed Sheeran" }
    Respuesta
    { "mensaje": "Preferencia agregada" }

- GET /usuarios/<id>/preferencias → Listar las preferencias de un usuario.
    Respuesta
    [ "Ed Sheeran", "Adele" ]


3. Spotify

- GET /spotify/info_artista?nombre=<nombre_artista> → Buscar un artista en Spotify y devolver:
+Nombre del artista
+Géneros
+Canción más popular
+Otras canciones
    Respuesta
    json { "artista": "Ed Sheeran", "generos": ["pop", "folk"], "cancion_mas_popular": "Shape of You", "otras_canciones": ["Perfect", "Photograph", "Thinking Out Loud", "Happier"] }

## Conclusiones

Este proyecto me permitio:

- Aprender a integrar Flask con APIs externas como Spotify.
- Manejos de entorno seguros con .env.
- Estructurar un rpoyecto profesionl listo para compartirse en GitHub.
- Comprender cómo crear endpoints RESTful y documentarlos adecuadamente.
- Realizar un CRUD y uso de mensaje como el 404 y 201


