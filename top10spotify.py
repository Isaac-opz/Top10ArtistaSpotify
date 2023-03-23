import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticación de la API de Spotify
client_id = 'f197b78781b24e389ed6b150642dd57c'
client_secret = 'f96b8432991146eabba9e7e9c2dffa83'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Búsqueda del artista
artist_name = 'juice wrld'
result = sp.search(artist_name, type='artist')

# Obtiene el id del artista
artist_id = result['artists']['items'][0]['id']

# Obtiene las canciones más escuchadas del artista
top_tracks = sp.artist_top_tracks(artist_id, country='US')

# Imprime las 10 canciones más escuchadas del artista
print(f"Las 10 canciones más escuchadas de {artist_name} son:")
for track in top_tracks['tracks'][:10]:
    print(f"- {track['name']}")
