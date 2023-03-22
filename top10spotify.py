import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
while True:
    # Ingresar las credenciales de tu aplicación de Spotify
    client_id = 'TU_CLIENT_ID'
    client_secret = 'TU_CLIENT_SECRET'

    # Autenticar con Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Buscar canciones por artista
    artista = input("Escribe el nombre del artista tal cual como aparece en spotify: \n")
    results = sp.search(q='artist:' + artista, type='track')

    # Mostrar los resultados
    print("Canciones del artista", artista, ":")
    for i, track in enumerate(results['tracks']['items'], start=1):
        print(f"{i}. {track['name']}")

    print('\n Las 10 canciones más escuchadas de hoy son: \n')

    # Obtener las 10 canciones más escuchadas hoy
    top_tracks = sp.playlist_tracks('37i9dQZEVXbMDoHDwVN2tF')

    # Mostrar los resultados
    for i, track in enumerate(top_tracks['items'][:10], start=1):
        print(f"{i}. {track['track']['name']} - {track['track']['artists'][0]['name']}")
