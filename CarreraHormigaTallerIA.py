import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# ---------------------------------------
# PARTE 1: Algoritmo Genético Evolutivo
# ---------------------------------------
def evolucionar_controlador(poblacion, tiempos):
    """Evoluciona el controlador del usuario según su desempeño."""
    # Fitness inverso al tiempo: menor tiempo = mayor fitness
    fitness = [1.0 / (t + 0.001) for t in tiempos]
    padres = np.argsort(fitness)[-2:]
    hijo = {
        'agresividad': np.mean([poblacion[p]['agresividad'] for p in padres]) + np.random.uniform(-0.05, 0.05),
        'conservador': np.mean([poblacion[p]['conservador'] for p in padres]) + np.random.uniform(-0.05, 0.05),
        'adelantamiento': np.mean([poblacion[p]['adelantamiento'] for p in padres]) + np.random.uniform(-0.05, 0.05)
    }
    # Mantener valores entre [0, 1]
    for k in hijo:
        hijo[k] = np.clip(hijo[k], 0, 1)
    poblacion[random.randint(0, len(poblacion)-1)] = hijo
    return poblacion, hijo

# Población inicial del usuario
poblacion_usuario = [
    {'agresividad': 0.4, 'conservador': 0.6, 'adelantamiento': 0.5},
    {'agresividad': 0.7, 'conservador': 0.3, 'adelantamiento': 0.6},
    {'agresividad': 0.5, 'conservador': 0.4, 'adelantamiento': 0.5}
]
controlador_usuario = poblacion_usuario[0]

# ---------------------------------------
# PARTE 2: PSO - Decisión de adelantamiento
# ---------------------------------------
class ControladorPSO:
    def decidir_adelantamiento(self, posicion, rivales, agresividad):
        for r in rivales:
            if np.linalg.norm(posicion - r) < 0.3 and agresividad > 0.5:
                return True
        return False

# ---------------------------------------
# PARTE 3: ACO - Feromonas (memoria de pista)
# ---------------------------------------
class HormigaRacing:
    def __init__(self, puntos):
        self.feromonas = np.ones(len(puntos))
    
    def reforzar_trayectoria(self, tramo, tiempo):
        self.feromonas[tramo] += 1.0 / (tiempo + 1)
        self.feromonas *= 0.999  # Evaporación

# ---------------------------------------
# PARTE 4: Configuración de pista y rivales
# ---------------------------------------
t = np.linspace(0, 4*np.pi, 200)
x_pista = np.cos(t) * (2 + 0.3*np.sin(4*t))
y_pista = np.sin(t) * (2 + 0.3*np.cos(3*t))
trayectoria = np.column_stack((x_pista, y_pista))

# Inicialización
robot_pos = np.array(trayectoria[0])
rivales = [
    {'pos': np.array(trayectoria[5]), 'color': 'red', 'nombre': 'Rival A', 'velocidad': 1.0},
    {'pos': np.array(trayectoria[10]), 'color': 'blue', 'nombre': 'Rival B', 'velocidad': 0.95},
    {'pos': np.array(trayectoria[15]), 'color': 'green', 'nombre': 'Rival C', 'velocidad': 0.9}
]

# ---------------------------------------
# PARTE 5: Simulación visual
# ---------------------------------------
fig = plt.figure(figsize=(9, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x_pista, y_pista, 'gray', lw=2)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_aspect('equal')
ax1.set_title('🏎️ Carrera Inteligente (Evolutiva)')

robot_dot, = ax1.plot([], [], 'yo', ms=10, label='Usuario')
rival_dots = [ax1.plot([], [], 'o', color=r['color'], ms=8)[0] for r in rivales]
texto = ax1.text(-2.8, 2.6, '', fontsize=10, color='black')

# Feromonas
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_xlim(0, len(trayectoria))
ax2.set_ylim(0, 5)
ax2.set_title('Feromonas (Aprendizaje del Usuario)')
barra_feromonas, = ax2.plot([], [], 'm-', lw=2)
ax2.set_xlabel('Punto en pista')
ax2.set_ylabel('Nivel de feromona')

# Inicializaciones
controlador_pso = ControladorPSO()
hormiga = HormigaRacing(trayectoria)
indice_robot = 0
vueltas = 10
tiempos_vueltas = []
contador_vueltas = 0
ganador = None

# ---------------------------------------
# PARTE 6: Función de animación
# ---------------------------------------
def animar(frame):
    global indice_robot, contador_vueltas, ganador, controlador_usuario, poblacion_usuario, tiempos_vueltas

    indice_robot = (indice_robot + 1) % len(trayectoria)
    robot_pos[:] = trayectoria[indice_robot]

    # Movimiento de rivales
    for r in rivales:
        idx = (np.where((trayectoria == r['pos']).all(axis=1))[0][0] + int(r['velocidad'] * 2)) % len(trayectoria)
        r['pos'] = trayectoria[idx]
    
    # Decisión PSO
    if controlador_pso.decidir_adelantamiento(robot_pos, [r['pos'] for r in rivales], controlador_usuario['agresividad']):
        robot_pos[:] = robot_pos + 0.05 * np.random.randn(2)
    
    # Refuerzo con feromonas
    hormiga.reforzar_trayectoria(indice_robot, frame + 1)
    
    # Actualizar posiciones
    robot_dot.set_data(robot_pos[0], robot_pos[1])
    for i, r in enumerate(rivales):
        rival_dots[i].set_data(r['pos'][0], r['pos'][1])
    
    # Detectar vueltas completadas
    if indice_robot == 0:
        contador_vueltas += 1
        tiempos_vueltas.append(frame)
        if contador_vueltas > 1:
            # Evolución genética del controlador según desempeño
            poblacion_usuario, controlador_usuario = evolucionar_controlador(poblacion_usuario, tiempos_vueltas)
            print(f"🏁 Nueva evolución del controlador: {controlador_usuario}")
        if contador_vueltas >= vueltas:
            # Evaluar quién gana (posición final)
            posiciones = {'Usuario': indice_robot}
            for r in rivales:
                idx = np.where((trayectoria == r['pos']).all(axis=1))[0][0]
                posiciones[r['nombre']] = idx
            ganador = max(posiciones, key=posiciones.get)
            print(f"🏆 El ganador es: {ganador}")
    
    texto.set_text(f"Vuelta: {min(contador_vueltas+1, vueltas)} / {vueltas}")
    barra_feromonas.set_data(np.arange(len(trayectoria)), hormiga.feromonas)
    ax2.set_ylim(0, max(hormiga.feromonas) * 1.2)

    return [robot_dot, *rival_dots, texto, barra_feromonas]

ani = animation.FuncAnimation(fig, animar, frames=len(trayectoria) * vueltas,
                              interval=50, blit=True, repeat=False)

plt.tight_layout()
plt.show()
