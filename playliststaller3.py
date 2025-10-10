import numpy as np
import random

# === EL REPERTORIO DE METALLICA ===
canciones = {
    'Enter Sandman': {'The black album': 0.1, 'energia': 0.95, 'valencia': 0.4},#1
    'Sad but true': {'The black album': 0.1, 'energia': 0.6, 'valencia': 0.7},
    'Holier than thou': {'The black album': 0.1, 'energia': 0.8, 'valencia': 0.5},
    'The Unforgiven': {'The black album': 0.1, 'energia': 0.4, 'valencia': 0.7},
    'Wherever i May Roam': {'The black album': 0.1, 'energia': 0.7, 'valencia': 0.2},
    'Dont tread on me': {'The black album': 0.1, 'energia': 0.8, 'valencia': 0.8},
    'Through the Never': {'The black album': 0.1, 'energia': 0.5, 'valencia': 0.2},
    'Nothing Else Matters': {'The black album': 0.1, 'energia': 0.2, 'valencia': 0.6},
    'Of Wolf And Man': {'The black album': 0.1, 'energia': 0.9, 'valencia': 0.5},
    'The God That Failed': {'The black album': 0.1, 'energia': 0.7, 'valencia': 0.8},
    'My friend Of misery': {'The black album': 0.1, 'energia': 0.6, 'valencia': 0.7},
    'The Struggle Within': {'The black album': 0.1, 'energia': 0.4, 'valencia': 0.3},

    'Hit The Lights': {'Kill Em all': 0.2, 'energia': 0.8, 'valencia': 0.7},#2
    'The Four Horsemen': {'Kill Em all': 0.2, 'energia': 0.4, 'valencia': 0.8},#2
    'Motorbreath': {'Kill Em all': 0.2, 'energia': 0.6, 'valencia': 0.6},#2
    'Jump in the Fire': {'Kill Em all': 0.2, 'energia': 0.3, 'valencia': 0.3},#2
    '(Anestresia) Pulling Teeth': {'Kill Em all': 0.2, 'energia': 0.3, 'valencia': 0.8},#2
    'Whiplash': {'Kill Em all': 0.2, 'energia': 0.8, 'valencia': 0.3},#2
    'Phantom Lord': {'Kill Em all': 0.2, 'energia': 0.6, 'valencia': 0.4},#2
    'No Remorse': {'Kill Em all': 0.2, 'energia': 0.4, 'valencia': 0.5},#2
    'Seek & Destroy': {'Kill Em all': 0.2, 'energia': 0.8, 'valencia': 0.2},#2
    'Metal Militia': {'Kill Em all': 0.2, 'energia': 0.9, 'valencia': 0.9},#2

    'That Was Just Your Life': {'Death Magnetic': 0.3, 'energia': 0.5, 'valencia': 0.7},#3
    'The End Of the Line': {'Death Magnetic': 0.3, 'energia': 0.5, 'valencia': 0.4},#3
    'Broken, Beat & Scarred': {'Death Magnetic': 0.3, 'energia': 0.6, 'valencia': 0.6},#3
    'The Day that Never Comes': {'Death Magnetic': 0.3, 'energia': 0.1, 'valencia': 0.5},#3
    'All nightmare long': {'Death Magnetic': 0.3, 'energia': 0.9, 'valencia': 0.2},#3
    'Cyanide': {'Death Magnetic': 0.3, 'energia': 0.7, 'valencia': 0.3},#3
    'The Unforgiven III': {'Death Magnetic': 0.3, 'energia': 0.5, 'valencia': 0.3},#3
    'The Judas Kiss': {'Death Magnetic': 0.3, 'energia': 0.3, 'valencia': 0.5},#3
    'Suicide & Redemption': {'Death Magnetic': 0.3, 'energia': 0.8, 'valencia': 0.7},#3
    'My Apocalypse': {'Death Magnetic': 0.3, 'energia': 0.3, 'valencia': 0.9},#3

    
    'Fuel': {'Reload': 0.4, 'energia': 0.7, 'valencia': 0.2},#4
    'The Memory Remains': {'Reload': 0.4, 'energia': 0.3, 'valencia': 0.9},#4
    'Devils Dance': {'Reload': 0.4, 'energia': 0.2, 'valencia': 0.7},#4
    'The Unforgiven II': {'Reload': 0.4, 'energia': 0.1, 'valencia': 0.5},#4
    'Better Than You': {'Reload': 0.4, 'energia': 0.3, 'valencia': 0.1},#4
    'Sliher': {'Reload': 0.4, 'energia': 0.2, 'valencia': 0.2},#4
    'Carpe Diem Baby': {'Reload': 0.4, 'energia': 0.3, 'valencia': 0.3},#4
    'Bad Seed': {'Reload': 0.4, 'energia': 0.1, 'valencia': 0.85},#4
    'Where The Wild Things Are': {'Reload': 0.4, 'energia': 0.2, 'valencia': 0.7},#4
    'Prince Charming': {'Reload': 0.4, 'energia': 0.3, 'valencia': 0.6},#4
    'Low Mans Lyric': {'Reload': 0.4, 'energia': 0.7, 'valencia': 0.6},#4
    'Attitude': {'Reload': 0.4, 'energia': 0.2, 'valencia': 0.8},#4
    'Fixxxer': {'Reload': 0.4, 'energia': 0.3, 'valencia': 0.5},#4


    'Ride the lighting': {'RTL': 0.5, 'energia': 0.9, 'valencia': 0.8},#5
    'Fight Fire with Fire': {'RTL': 0.5, 'energia': 0.8, 'valencia': 0.4},#5
    'From Whom the Bell Tolls': {'RTL': 0.5, 'energia': 0.3, 'valencia': 0.1},#5
    'Escape': {'RTL': 0.5, 'energia': 0.4, 'valencia': 0.3},#5
    'Trapped Under Ice': {'RTL': 0.5, 'energia': 0.7, 'valencia': 0.5},#5
    'Creeping Death': {'RTL': 0.5, 'energia': 0.8, 'valencia': 0.5},#5
    'The Call Of Ktulu': {'RTL': 0.5, 'energia': 0.2, 'valencia': 0.2},#5
    'Fade to Black': {'RTL': 0.5, 'energia': 0.1, 'valencia': 0.7},#5


    '72 Seasons': {'72 seasons': 0.6, 'energia': 0.8, 'valencia': 0.3},#6
    'Shadows Follow': {'72 seasons': 0.6, 'energia': 0.4, 'valencia': 0.9},#6
    'Screaming Suicide': {'72 seasons': 0.6, 'energia': 0.3, 'valencia': 0.5},#6
    'Sleepwalk My Life Away': {'72 seasons': 0.6, 'energia': 0.2, 'valencia': 0.7},#6
    'You Must Burn!': {'72 seasons': 0.6, 'energia': 0.5, 'valencia': 0.9},#6
    'Lux AEterna': {'72 seasons': 0.6, 'energia': 0.8, 'valencia': 0.8},#6
    'Crown of Barbed Wire': {'72 seasons': 0.6, 'energia': 0.7, 'valencia': 0.5},#6
    'Chasing Light': {'72 seasons': 0.6, 'energia': 0.3, 'valencia': 0.4},#6
    'If darkness Had a Son': {'72 seasons': 0.6, 'energia': 0.5, 'valencia': 0.8},#6
    'Too Far Gone?': {'72 seasons': 0.6, 'energia': 0.1, 'valencia': 0.2},#6
    'Room of Mirrors': {'72 seasons': 0.6, 'energia': 0.1, 'valencia': 0.2},#6
    'Inamorata': {'72 seasons': 0.6, 'energia': 0.1, 'valencia': 0.2},#6



    'Battery': {'MOP': 0.7, 'energia': 0.9, 'valencia': 0.8},#7
    'Master of Puppets': {'MOP': 0.7, 'energia': 0.9, 'valencia': 0.3},#7
    'The Thing That Should Not Be': {'MOP': 0.7, 'energia': 0.4, 'valencia': 0.2},#7
    'Welcome Home (Sanitarium)': {'MOP': 0.7, 'energia': 0.2, 'valencia': 0.7},#7
    'Disposable Heroes': {'MOP': 0.7, 'energia': 0.8, 'valencia': 0.4},#7
    'Lepper Messiah': {'MOP': 0.7, 'energia': 0.5, 'valencia': 0.5},#7
    'Orion': {'MOP': 0.7, 'energia': 0.2, 'valencia': 0.9},#7
    'Damage.Inc': {'MOP': 0.7, 'energia': 0.2, 'valencia': 0.8},#7

    'One': {'And justice for all': 0.8, 'energia': 0.95, 'valencia': 0.7},#8
    'Blackened': {'And justice for all': 0.8, 'energia': 0.9, 'valencia': 0.3},#8
    '...And Justice For All': {'And justice for all': 0.5, 'energia': 0.95, 'valencia': 0.2},#8
    'Eye Of The Beholder': {'And justice for all': 0.3, 'energia': 0.95, 'valencia': 0.2},#8
    'The Shortest Straw': {'And justice for all': 0.7, 'energia': 0.95, 'valencia': 0.5},#8
    'Harvester of Sorrow': {'And justice for all': 0.8, 'energia': 0.95, 'valencia': 0.4},#8
    'The Frayed Ends of Sanity': {'And justice for all': 0.2, 'energia': 0.95, 'valencia': 0.3},#8
    'To live is to Die': {'And justice for all': 0.8, 'energia': 0.4, 'valencia': 0.9},#8
    'Dyers Eve': {'And justice for all': 0.8, 'energia': 0.5, 'valencia': 0.1},#8

    'Astronomy': {'garage.inc': 0.9, 'energia': 0.9, 'valencia': 0.8},#9
    'Free Speech For The Dumb': {'garage.inc': 0.5, 'energia': 0.9, 'valencia': 0.1},#9
    'Its Electric': {'garage.inc': 0.9, 'energia': 0.2, 'valencia': 0.8},#9
    'Sabbra Cadabra': {'garage.inc': 0.9, 'energia': 0.1, 'valencia': 0.3},#9
    'Turn The Page': {'garage.inc': 0.9, 'energia': 0.5, 'valencia': 0.1},#9
    'Die, Die my Darling': {'garage.inc': 0.9, 'energia': 0.8, 'valencia': 0.3},#9
    'Loverman': {'garage.inc': 0.9, 'energia': 0.8, 'valencia': 0.5},#9
    'Mercyful Fate': {'garage.inc': 0.9, 'energia': 0.6, 'valencia': 0.8},#9
    'Whiskey In The Jar': {'garage.inc': 0.9, 'energia': 0.3, 'valencia': 0.6},#9
    'Tuesdays Gone': {'garage.inc': 0.9, 'energia': 0.1, 'valencia': 0.8},#9
    'The More I See': {'garage.inc': 0.9, 'energia': 0.4, 'valencia': 0.5},#9
    'Helpless': {'garage.inc': 0.9, 'energia': 0.7, 'valencia': 0.3},#9
    'The Small Hours': {'garage.inc': 0.9, 'energia': 0.4, 'valencia': 0.3},#9
    'The Wait': {'garage.inc': 0.9, 'energia': 0.2, 'valencia': 0.2},#9
    'Crash Course In Brain Surgery': {'garage.inc': 0.1, 'energia': 0.9, 'valencia': 0.4},#9
    'Last Careless / Green Hell': {'garage.inc': 0.2, 'energia': 0.9, 'valencia': 0.6},#9
    'Am I Evil?': {'garage.inc': 0.9, 'energia': 0.5, 'valencia': 0.85},#9
    'Blitzkrieg': {'garage.inc': 0.9, 'energia': 0.5, 'valencia': 0.8},#9
    'Breadfan': {'garage.inc': 0.9, 'energia': 0.9, 'valencia': 0.5},#9
    'The Prince': {'garage.inc': 0.9, 'energia': 0.7, 'valencia': 0.6},#9
    'Stone Cold Crazy': {'garage.inc': 0.9, 'energia': 0.4, 'valencia': 0.8},#9
    'So What': {'garage.inc': 0.9, 'energia': 0.5, 'valencia': 0.7},#9
    'Killing Time': {'garage.inc': 0.9, 'energia': 0.2, 'valencia': 0.85},#9

    'Frantic': {'st.anger': 0.95, 'energia': 0.6, 'valencia': 0.9},#10
    'St.Anger': {'st.anger': 0.95, 'energia': 0.4, 'valencia': 0.4},#10
    'Some Kind of Monster': {'st.anger': 0.95, 'energia': 0.5, 'valencia': 0.5},#10
    'Dirty Window': {'st.anger': 0.95, 'energia': 0.6, 'valencia': 0.2},#10
    'Invisible Kid': {'st.anger': 0.95, 'energia': 0.1, 'valencia': 0.1},#10
    'My World': {'st.anger': 0.95, 'energia': 0.5, 'valencia': 0.5},#10
    'Shoot Me Again': {'st.anger': 0.95, 'energia': 0.2, 'valencia': 0.3},#10
    'Sweet Amber': {'st.anger': 0.95, 'energia': 0.3, 'valencia': 0.5},#10
    'The Unnamed Feeling': {'st.anger': 0.95, 'energia': 0.6, 'valencia': 0.2},#10
    'Purify': {'st.anger': 0.95, 'energia': 0.2, 'valencia': 0.6},#10
    'All within My Hands': {'st.anger': 0.95, 'energia': 0.5, 'valencia': 0.8},#10


    'Aint my Bitch': {'load': 0.99, 'energia': 0.7, 'valencia': 0.3},#11
    '2x4': {'load': 0.99, 'energia': 0.7, 'valencia': 0.3},#11
    'The House Jack Built': {'load': 0.99, 'energia': 0.7, 'valencia': 0.1},#11
    'Ultin It Sleeps': {'load': 0.99, 'energia': 0.5, 'valencia': 0.8},#11
    'King nothing': {'load': 0.99, 'energia': 0.1, 'valencia': 0.7},#11
    'Hero of the Day': {'load': 0.99, 'energia': 0.9, 'valencia': 0.2},#11
    'Bleeding Me': {'load': 0.99, 'energia': 0.5, 'valencia': 0.5},#11
    'Cure': {'load': 0.99, 'energia': 0.5, 'valencia': 0.4},#11
    'Poor Twisted Me': {'load': 0.99, 'energia': 0.1, 'valencia': 0.6},#11
    'Wasting My Hate': {'load': 0.99, 'energia': 0.2, 'valencia': 0.5},#11
    'Mama Said': {'load': 0.99, 'energia': 0.6, 'valencia': 0.2},#11
    'Ronnie': {'load': 0.99, 'energia': 0.4, 'valencia': 0.1},#11
    'Thorn Within': {'load': 0.99, 'energia': 0.3, 'valencia': 0.4},#11
    'The Outlaw Torn': {'load': 0.99, 'energia': 0.4, 'valencia': 0.8},#11
    
    'Hardwired': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.5, 'valencia': 0.9},#12
    'Atlas, Rise!': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.6, 'valencia': 0.5},#12
    'Now That Were Dead': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.9, 'valencia': 0.4},#12
    'Moth Into Flame': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.8, 'valencia': 0.7},#12
    'Dream No More': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.3, 'valencia': 0.1},#12
    'Halo On Fire': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.1, 'valencia': 0.5},#12
    'Confusion': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.3, 'valencia': 0.7},#12
    'manUNkind': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.4, 'valencia': 0.8},#12
    'Here comes Revenge': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.5, 'valencia': 0.9},#12
    'Am I Savage?': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.8, 'valencia': 0.4},#12
    'Murder One': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.5, 'valencia': 0.1},#12
    'Spit out the Bone': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.4, 'valencia': 0.8},#12
    'Lords Of Summer': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.5, 'valencia': 0.2},#12
    'Ronnie Rising Medley': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.2, 'valencia': 0.4},#12
    'When a Blind Man Cries': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.5, 'valencia': 0.6},#12
    'Remember Tomorrow': {'Hardwired to Selfdesctruct': 0.15, 'energia': 0.8, 'valencia': 0.8},#12
}

# === PREFERENCIAS DEL USUARIO ===
preferencias_usuario = {'RTL': 0.5, 'energia': 0.8, 'valencia': 0.7}

# === FUNCIONES DE SIMILITUD Y AFINIDAD ===
def afinidad_usuario(cancion, preferencias):
    v1 = np.array([cancion.get(k, 0) for k in preferencias])
    v2 = np.array(list(preferencias.values()))
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)

def similitud(c1, c2):
    atributos = list(set(c1.keys()) | set(c2.keys()))
    v1 = np.array([c1.get(k, 0) for k in atributos])
    v2 = np.array([c2.get(k, 0) for k in atributos])
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)

# === PARÁMETROS DEL ACO ===
canciones_lista = list(canciones.keys())
pheromone = {(i, j): 1.0 for i in canciones_lista for j in canciones_lista if i != j}

NUM_HORMIGAS = 20
NUM_ITER = 50
ALPHA = 1
BETA = 2
RHO = 0.3
Q = 100

def probabilidad(cancion_actual, posibles):
    tau = np.array([pheromone.get((cancion_actual, j), 1.0) for j in posibles])
    eta = np.array([similitud(canciones[cancion_actual], canciones[j]) for j in posibles])
    numerador = (tau ** ALPHA) * (eta ** BETA)
    return numerador / (numerador.sum() + 1e-9)

def construir_playlist(start, longitud=8):
    playlist = [start]
    actual = start
    while len(playlist) < longitud:
        posibles = [c for c in canciones_lista if c not in playlist]
        if not posibles:
            break
        probs = probabilidad(actual, posibles)
        siguiente = random.choices(posibles, weights=probs, k=1)[0]
        playlist.append(siguiente)
        actual = siguiente
    return playlist

def calidad_playlist(playlist):
    return np.mean([afinidad_usuario(canciones[s], preferencias_usuario) for s in playlist])

def actualizar_feromonas(playlists):
    global pheromone
    for edge in pheromone:
        pheromone[edge] *= (1 - RHO)
    for playlist in playlists:
        QL = Q * calidad_playlist(playlist)
        for i in range(len(playlist) - 1):
            a, b = playlist[i], playlist[i+1]
            pheromone[(a, b)] += QL

# === EJECUCIÓN DEL ACO ===
mejor_playlist = None
mejor_calidad = -1

for it in range(NUM_ITER):
    playlists = []
    for _ in range(NUM_HORMIGAS):
        start = random.choice(canciones_lista)
        pl = construir_playlist(start)
        playlists.append(pl)
        q = calidad_playlist(pl)
        if q > mejor_calidad:
            mejor_playlist = pl
            mejor_calidad = q
    actualizar_feromonas(playlists)
    print(f"Iter {it+1}: mejor calidad = {mejor_calidad:.3f}")

print("\n🎶 Playlist recomendada:")
for s in mejor_playlist:
    print(f"reproducir {s}: {canciones[s]}")
