**TALLER2CORTE**
# 🧠 Simulación de Carrera Inteligente con Algoritmos Evolutivos, PSO y ACO

Este proyecto implementa una **simulación interactiva de una carrera** en la que un “robot piloto” aprende y mejora su comportamiento a medida que avanza la competencia.  
Se utilizan principios de **algoritmos genéticos**, **PSO (Particle Swarm Optimization)** y **ACO (Ant Colony Optimization)** para modelar la toma de decisiones y el aprendizaje de la trayectoria.

---

## 📌 Objetivos del Proyecto

- Simular una carrera entre un **usuario inteligente** y varios rivales.  
- **Evolucionar el comportamiento del controlador** del usuario a lo largo de múltiples vueltas.  
- Tomar decisiones de adelantamiento basadas en PSO.  
- Reforzar trayectorias óptimas mediante ACO.  
- Visualizar en tiempo real la pista, las posiciones y el aprendizaje con feromonas.

---

## 🧬 1. Algoritmo Genético (Evolución del Controlador)

La población inicial contiene diferentes configuraciones de parámetros de conducción:
- `agresividad`
- `conservador`
- `adelantamiento`

Cada vuelta completada evalúa el **tiempo de desempeño**, y el algoritmo selecciona los mejores individuos para generar un nuevo controlador mediante:
- Selección de padres (mejor fitness)
- Cruce (promedio de atributos)
- Mutación aleatoria controlada
- Clipping de valores en `[0, 1]`

📈 **Resultado:** El controlador del usuario se adapta automáticamente para optimizar su rendimiento en la carrera.

---

## 🐦 2. PSO - Decisiones de Adelantamiento

La clase `ControladorPSO` evalúa:
- Posición actual del robot
- Posiciones de rivales
- Nivel de agresividad

Si hay un rival cerca y el controlador es lo suficientemente agresivo, el usuario **toma la decisión de adelantar**, añadiendo aleatoriamente una pequeña variación en su posición.

🧠 **Comportamiento emergente:** conductores más agresivos adelantan con mayor frecuencia.

---

## 🐜 3. ACO - Feromonas y Aprendizaje de Trayectoria

La clase `HormigaRacing` implementa un sistema de **feromonas** para modelar memoria colectiva:
- Cada punto recorrido refuerza la cantidad de feromona.
- Las feromonas se evaporan con el tiempo.
- Las trayectorias más rápidas se vuelven más “atractivas”.

📊 La segunda gráfica muestra en tiempo real cómo evoluciona el nivel de feromonas a lo largo de la pista.

---

## 🏁 4. Configuración de la Pista y Rivales

- La pista se genera con una trayectoria curva usando funciones trigonométricas.  
- Se ubican tres rivales con velocidades diferentes (`1.0`, `0.95` y `0.9`) para simular competencia.  
- El robot inicia en la primera posición de la trayectoria.

---

## 🎥 5. Visualización de la Simulación

- **Panel Izquierdo:** Vista en planta de la pista, robot (amarillo) y rivales (rojo, azul, verde).  
- **Panel Derecho:** Nivel de feromonas a lo largo de los puntos de la pista.  
- Se muestran las vueltas actuales y la evolución del controlador.

La animación se gestiona con `matplotlib.animation.FuncAnimation`.

---

## 🔁 6. Evolución Durante la Carrera

Cada vuelta completada:
- Se guarda el tiempo.
- Se evalúa el rendimiento.
- Se actualiza el controlador usando algoritmo genético.
- Se refuerzan feromonas.

Cuando se alcanzan las vueltas definidas:
- Se determina el **ganador** comparando posiciones finales.
- Se imprime el controlador evolucionado final.

---

## 🧰 Tecnologías Utilizadas

- `numpy` → Cálculos numéricos  
- `matplotlib` → Visualización y animación  
- `random` → Mutación estocástica  
- Algoritmos de IA: **GA**, **PSO**, **ACO**

---

## 🏎️ Ejecución

```bash
python carrera_evolutiva.py
