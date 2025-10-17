# 🧬 Simulación Evolutiva de Pokémon — Algoritmo Genético y Análisis de Tipos

Este proyecto implementa un **modelo evolutivo de criaturas tipo Pokémon**, en el que un individuo inicial evoluciona a través de múltiples generaciones para optimizar sus estadísticas y afinidades de tipo.  
Se utiliza un **algoritmo genético** para simular procesos de mejora y selección natural, además de cálculos de efectividad ofensiva y defensiva.

---

## 📌 Objetivos Principales

- Generar un **Pokémon base** con tipo primario, secundario y naturaleza.  
- Simular un proceso evolutivo basado en **algoritmos genéticos** durante varias generaciones.  
- Analizar la **efectividad ofensiva y defensiva** según combinaciones de tipos.  
- Visualizar gráficamente el **progreso del fitness** y la efectividad final.

---

## 🧠 1. Definición de Tipos y Efectividad

- Se definen 18 tipos elementales (fuego, agua, planta, etc.).  
- Se implementa una **tabla de efectividad** que determina cuánto daño hace cada tipo contra otro.  
- La función `mult()` devuelve el multiplicador de efectividad en un combate tipo-atacante vs. tipo-defensor.

🔸 *Ejemplo:* fuego → planta = 2.0 (súper efectivo)

---

## 🌿 2. Naturalezas

Cada naturaleza afecta **positiva y negativamente** ciertas estadísticas:

| Naturaleza | ↑ Stat Beneficiada | ↓ Stat Afectada |
|------------|--------------------|------------------|
| Fuerte     | Ataque             | —                |
| Miedosa    | Velocidad          | Ataque           |
| Serena     | Defensa Especial   | Ataque           |
| ...        | ...                | ...              |

👉 Esto permite crear individuos con comportamientos estratégicos distintos.

---

## ⚔️ 3. Sinergia de Tipos (Tipo Secundario)

La función `elegir_tipo_secundario()` selecciona el tipo secundario **óptimo** para complementar el primario considerando:
- Ganancia ofensiva adicional (más tipos cubiertos).
- Resistencia adicional a debilidades.
- Penalización por nuevas debilidades introducidas.

📈 *Resultado:* un tipo secundario sinérgico que maximiza cobertura y defensa.

---

## 🧬 4. Individuos y Fitness

Cada Pokémon tiene:
- 6 estadísticas base (`ataque`, `defensa`, `velocidad`, `ataque_esp`, `defensa_esp`, `vida`).  
- IVs aleatorios (0–31).  
- Naturaleza.  
- Tipos primario y secundario.

El **fitness** se calcula considerando:
- Promedio de estadísticas + IVs  
- Efectividad ofensiva (promedio de multiplicadores de ataque)  
- Efectividad defensiva (inmunidades, resistencias, debilidades)

📊 Esto permite evaluar qué tan "bueno" es un Pokémon en combate.

---

## 🧪 5. Algoritmo Genético

La función `evolucion_genetica()` simula generaciones:
1. **Población inicial** basada en un individuo base.  
2. **Selección** de los mejores individuos según fitness.  
3. **Cruce** (mezcla de genes) y **mutación aleatoria** para generar nuevos.  
4. **Elitismo** para mantener a los mejores.  
5. **Repetición** durante varias generaciones (por defecto 50 por evolución).

📌 Cada evolución mejora progresivamente el fitness promedio de la población.

---

## 🛡️ 6. Análisis Defensivo

La función `tabla_defensiva()` calcula cómo el Pokémon recibe daño de cada tipo:
- **Inmunidades:** multiplicador 0  
- **Resistencias:** multiplicador < 1  
- **Debilidades:** multiplicador > 1

Se genera una tabla y un gráfico de barras codificado por colores:
- 🟩 Verde = resistencia  
- ⚪ Gris = neutral  
- 🔴 Rojo = debilidad

---

## 🗡️ 7. Análisis Ofensivo

La función `tabla_ofensiva()` calcula el poder de ataque contra cada tipo:
- **Súper efectivo:** > 1  
- **Neutral:** = 1  
- **No efectivo:** = 0  
- **Poco efectivo:** < 1

Se genera un gráfico de barras con colores diferenciados.

---

## 📈 8. Visualización Gráfica

Se muestran dos gráficos principales:
- Evolución del **fitness total** a lo largo de las generaciones.  
- Distribución **defensiva y ofensiva** por tipo.  

---

## 🏆 9. Resultado Final

Al finalizar las 5 evoluciones:

- Se imprimen las estadísticas finales y IVs.
- Se muestran tablas ofensivas y defensivas.
- Se guardan gráficas de efectividad ofensiva.
- El Pokémon final es el individuo con mejor fitness total.

---

## 🧰 Tecnologías Utilizadas

- `numpy` → cálculos numéricos
- `random` y `copy` → variación genética
- `matplotlib` → visualización y gráficos
- `pandas` → tablas de efectividad
