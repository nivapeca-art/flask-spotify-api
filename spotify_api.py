from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app=Flask (__name__)

CLIENT_ID = "6d4f4a619dac4c7d9f474585d64781e9"
CLIENT_SECRET = "51a259fc98d243b5816b6bcd57f3bd9c"

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)

usuarios = {}
preferencias = {}
contador_id = 1

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    global contador_id
    data = request.get_json()

    if"nombre" not in data or "edad" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}),400
    
    usuario = {
        "id": contador_id,
        "nombre": data["nombre"],
        "edad": data["edad"]
    }
    usuarios[contador_id] = usuario
    preferencias[contador_id] = []

    contador_id += 1
    return jsonify(usuario), 201

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(list(usuarios.values()))

@app.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    if id not in usuarios:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuarios[id])

@app.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    if id not in usuarios:
        return jsonify ({"error": "Usuario no encontrado"}),404
    data= request.get_json()
    usuarios[id].update(data)
    return jsonify(usuarios[id])

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    if id not in usuarios:
        return jsonify ({"error": "Usuario no encontrado"}), 404
    del usuarios[id]
    preferencias.pop(id, None)
    return jsonify ({"mensaje":"Usuario eliminado"})

@app.route("/usuarios/<int:id>/preferencias", methods=["POST"])
def agregar_preferencia(id):
    if id not in usuarios:
        return jsonify ({"error":"Usuario no encontrado"}), 404
    data = request.get_json()
    if "artista" not in data:
        return jsonify ({"error":"Falta el artista"}), 404
    
    preferencias[id].append(data["artista"])
    return jsonify({"mensaje":"Preferencia agregada"})

@app.route("/usuarios/<int:id>/preferencias",methods=["GET"])
def obtener_preferencia(id):
    if id not in usuarios:
        return jsonify ({"error":"Usuario no encontrado"})
    return jsonify(preferencias[id])

@app.route("/spotify/info_artista")
def info_artista():
    nombre=request.args.get("nombre")
    if not nombre:
        return jsonify({"error":"Falta el 'nombre'"}), 400
    
    artista_resultado=sp.search(q=nombre, type="artist", limit=1)
    if not artista_resultado["artists"]["items"]:
        return jsonify ({"error":"Artista no encontrado"}),404
    artista=artista_resultado["artists"]["items"][0]
    artista_id=artista["id"]
    artista_nombre=artista["name"]
    genero=artista.get("genres",[])

    top_tracks_result=sp.artist_top_tracks(artista_id)
    tracks=top_tracks_result.get("tracks",[])

    if not tracks:
        return jsonify ({"error":"No se encontraron canciones"}), 404
    
    cancion_popular=tracks[0]["name"]
    otras_canciones=[t["name"]for t in tracks[1:5]]

    return jsonify({
        "artista":artista_nombre,
        "generos":genero,
        "cancion_mas_popular":cancion_popular,
        "otras_canciones":otras_canciones
    })
if __name__=="__main__":
    app.run(debug=True)