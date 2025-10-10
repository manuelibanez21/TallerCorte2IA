# pokemon_evolucion_completa_v3.py
import random
import copy
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------
# Tipos y tabla de efectividad
# -----------------------
TIPOS = [
    "normal","fuego","agua","planta","electrico","hielo","lucha","veneno",
    "tierra","volador","psiquico","bicho","roca","fantasma","dragon","siniestro",
    "acero","hada"
]

EFECTIVIDAD = {
    "normal":   {"roca":0.5, "fantasma":0.0, "acero":0.5},
    "fuego":    {"fuego":0.5,"agua":0.5,"planta":2,"hielo":2,"bicho":2,"roca":0.5,"dragon":0.5,"acero":2},
    "agua":     {"fuego":2,"agua":0.5,"planta":0.5,"tierra":2,"roca":2,"dragon":0.5},
    "planta":   {"fuego":0.5,"agua":2,"planta":0.5,"veneno":0.5,"tierra":2,"volador":0.5,"bicho":0.5,"roca":2,"dragon":0.5,"acero":0.5},
    "electrico":{"agua":2,"volador":2,"electrico":0.5,"planta":0.5,"dragon":0.5,"tierra":0.0},
    "hielo":    {"fuego":0.5,"agua":0.5,"planta":2,"tierra":2,"volador":2,"dragon":2,"acero":0.5},
    "lucha":    {"normal":2,"hielo":2,"roca":2,"siniestro":2,"acero":2,"veneno":0.5,"volador":0.5,"psiquico":0.5,"bicho":0.5,"hada":0.5,"fantasma":0.0},
    "veneno":   {"planta":2,"hada":2,"veneno":0.5,"tierra":0.5,"roca":0.5,"fantasma":0.5,"acero":0.0},
    "tierra":   {"fuego":2,"electrico":2,"veneno":2,"roca":2,"acero":2,"planta":0.5,"bicho":0.5,"volador":0.0},
    "volador":  {"planta":2,"lucha":2,"bicho":2,"electrico":0.5,"roca":0.5,"acero":0.5},
    "psiquico": {"lucha":2,"veneno":2,"psiquico":0.5,"acero":0.5,"siniestro":0.0},
    "bicho":    {"planta":2,"psiquico":2,"siniestro":2,"fuego":0.5,"lucha":0.5,"volador":0.5,"fantasma":0.5,"acero":0.5,"hada":0.5},
    "roca":     {"fuego":2,"hielo":2,"volador":2,"bicho":2,"lucha":0.5,"tierra":0.5,"acero":0.5},
    "fantasma": {"fantasma":2,"psiquico":2,"siniestro":0.5,"normal":0.0},
    "dragon":   {"dragon":2,"acero":0.5,"hada":0.0},
    "siniestro":{"psiquico":2,"fantasma":2,"lucha":0.5,"siniestro":0.5,"hada":0.5},
    "acero":    {"hielo":2,"roca":2,"hada":2,"fuego":0.5,"agua":0.5,"electrico":0.5,"acero":0.5},
    "hada":     {"lucha":2,"dragon":2,"siniestro":2,"fuego":0.5,"veneno":0.5,"acero":0.5}
}

def mult(atacante, defensor):
    return EFECTIVIDAD.get(atacante, {}).get(defensor, 1.0)

# -----------------------
# Naturalezas
# -----------------------
NATURALEZAS = {
    'Fuerte': ('ataque', None),
    'Osada': ('defensa', 'ataque'),
    'Miedosa': ('velocidad', 'ataque'),
    'Modesta': ('ataque_esp', 'ataque'),
    'Serena': ('defensa_esp', 'ataque'),
    'Huraña': ('ataque', 'defensa'),
    'Activa': ('velocidad', 'defensa'),
    'Audaz': ('ataque', 'velocidad'),
    'Plácida': ('defensa', 'velocidad'),
    'Mansa': ('ataque_esp', 'velocidad'),
    'Firme': ('ataque', 'ataque_esp'),
    'Agitada': ('defensa', 'ataque_esp'),
    'Alegre': ('velocidad', 'ataque_esp'),
    'Tímida': ('velocidad', 'ataque'),
    'Cauta': ('defensa_esp', 'ataque_esp'),
    'Pícara': ('ataque', 'defensa_esp'),
    'Floja': ('defensa', 'defensa_esp'),
    'Rara': (None, None)
}

# -----------------------
# Elegir tipo secundario en base a sinergia
# -----------------------
def elegir_tipo_secundario(tipo_primario):
    mejor = None
    mejor_score = -1e9
    prim = tipo_primario.lower()
    for candidato in TIPOS:
        if candidato == prim:
            continue
        sup_cand = {t for t,v in EFECTIVIDAD.get(candidato, {}).items() if v>1}
        sup_prim = {t for t,v in EFECTIVIDAD.get(prim, {}).items() if v>1}
        offensive_gain = len(sup_cand - sup_prim)
        prim_debles = {t for t in TIPOS if mult(t, prim) > 1.0}
        cand_resists = {t for t in TIPOS if mult(t, candidato) < 1.0}
        cand_inm = {t for t in TIPOS if mult(t, candidato) == 0.0}
        resist_gain = len(prim_debles & (cand_resists | cand_inm))
        cand_debles = {t for t in TIPOS if mult(t, candidato) > 1.0}
        prim_resists = {t for t in TIPOS if mult(t, prim) < 1.0}
        extra_weak = len(cand_debles - prim_resists)
        score = 1.2*offensive_gain + 1.0*resist_gain - 1.5*extra_weak
        if score > mejor_score:
            mejor_score = score
            mejor = candidato
    return mejor

# -----------------------
# Crear individuo
# -----------------------
def crear_individuo(nombre, tipo_prim, tipo_sec, naturaleza):
    stats = {k: random.uniform(0.3,0.7) for k in ["ataque","defensa","velocidad","ataque_esp","defensa_esp","vida"]}
    ivs = {k: random.randint(0,31) for k in stats}
    return {"nombre": nombre,"tipo1": tipo_prim,"tipo2": tipo_sec,"naturaleza": naturaleza,"stats": stats,"ivs": ivs}

# -----------------------
# Fitness
# -----------------------
def evaluar(ind):
    s = copy.deepcopy(ind["stats"])
    subir, bajar = NATURALEZAS[ind["naturaleza"]]
    if subir: s[subir] *= 1.10
    if bajar: s[bajar] *= 0.90
    stat_mean = sum((s[k] + ind["ivs"][k]/31.0) for k in s)/len(s)
    mults = [max(mult(ind["tipo1"],d), mult(ind["tipo2"],d)) for d in TIPOS]
    offense_avg = sum(mults)/len(mults)
    mult_recibidos = [mult(a, ind["tipo1"])*mult(a, ind["tipo2"]) for a in TIPOS]
    defensa_score = 1.0 / (1.0 + (sum(mult_recibidos)/len(mult_recibidos)-1.0))
    return stat_mean * (0.7 + 0.5*(offense_avg-1.0)) * (0.9 + 0.6*defensa_score)

# -----------------------
# Cruzamiento y mutación
# -----------------------
def cruzar(p1, p2):
    hijo = copy.deepcopy(p1)
    for k in hijo["stats"]:
        hijo["stats"][k] = random.choice([p1["stats"][k], p2["stats"][k]])
    for k in hijo["ivs"]:
        hijo["ivs"][k] = random.choice([p1["ivs"][k], p2["ivs"][k]])
    return hijo

def mutar(ind, prob=0.12):
    for k in ind["stats"]:
        if random.random() < prob:
            ind["stats"][k] = min(max(ind["stats"][k]+random.uniform(-0.06,0.06),0.01),1.0)
    for k in ind["ivs"]:
        if random.random() < 0.04:
            ind["ivs"][k] = min(max(ind["ivs"][k]+random.randint(-3,3),0),31)
    return ind

# -----------------------
# Algoritmo genético
# -----------------------
def evolucion_genetica(base_ind, generaciones=50, tam=30, elites=6):
    pobl = [copy.deepcopy(base_ind) for _ in range(tam)]
    for p in pobl[1:]:
        for k in p["stats"]:
            p["stats"][k] = min(max(p["stats"][k]+random.uniform(-0.08,0.08),0.01),1.0)
        p["ivs"] = {k: random.randint(0,31) for k in p["ivs"]}
    historico_best = []
    for g in range(generaciones):
        pobl.sort(key=evaluar, reverse=True)
        historico_best.append(evaluar(pobl[0]))
        nuevos = pobl[:elites]
        while len(nuevos)<tam:
            p1,p2=random.sample(pobl[:12],2)
            hijo=mutar(cruzar(p1,p2))
            nuevos.append(hijo)
        pobl=nuevos
    pobl.sort(key=evaluar, reverse=True)
    return pobl[0], historico_best

# -----------------------
# Tabla defensiva
# -----------------------
def tabla_defensiva(tipo1, tipo2):
    mults = {a: mult(a,tipo1)*mult(a,tipo2) for a in TIPOS}
    inmune = [t for t,v in mults.items() if v==0]
    res = [t for t,v in mults.items() if 0<v<1]
    neu = [t for t,v in mults.items() if v==1]
    deb = [t for t,v in mults.items() if v>1]
    return mults, inmune, res, neu, deb

# -----------------------
# Tabla ofensiva
# -----------------------
def tabla_ofensiva(tipo1, tipo2):
    mults = {d: max(mult(tipo1,d), mult(tipo2,d)) for d in TIPOS}
    super_eff = [t for t,v in mults.items() if v>1]
    neutral = [t for t,v in mults.items() if v==1]
    not_eff = [t for t,v in mults.items() if v==0]
    poco = [t for t,v in mults.items() if 0<v<1]
    return mults, super_eff, neutral, poco, not_eff

# -----------------------
# MAIN
# -----------------------
def main():
    print("=== Simulación Evolutiva Pokémon con Evoluciones ===\n")
    nombre = input("Nombre del Pokémon: ").strip()
    tipo_primario = input(f"Elige tipo primario:\n{', '.join(TIPOS)}\n→ ").strip().lower()
    if tipo_primario not in TIPOS:
        tipo_primario = "fuego"
    naturaleza = random.choice(list(NATURALEZAS.keys()))
    tipo_secundario = elegir_tipo_secundario(tipo_primario)

    print(f"\nNaturaleza asignada: {naturaleza}")
    print(f"Tipo Primario: {tipo_primario} | Tipo Secundario: {tipo_secundario}\n")

    individuo = crear_individuo(nombre, tipo_primario, tipo_secundario, naturaleza)
    fitness_hist_total = []

    for evo in range(1, 6):
        mejor, hist = evolucion_genetica(individuo, generaciones=50, tam=30, elites=6)
        fitness_hist_total.extend(hist)
        individuo = mejor
        print(f"→ Evolución {evo} completada | Mejor fitness: {evaluar(mejor):.4f}")

    # Tabla final de stats
    print("\n=== Estadísticas Finales ===")
    for k,v in individuo["stats"].items():
        print(f"{k.capitalize():15s}: {v:.3f}  (IV: {individuo['ivs'][k]})")

    # Tabla de tipos defensiva
    mults_def, inm, res, neu, deb = tabla_defensiva(individuo["tipo1"], individuo["tipo2"])
    df_def = pd.DataFrame([{"Atacante":a, "Multiplicador":m} for a,m in mults_def.items()]).sort_values("Multiplicador", ascending=False)
    print("\n=== Tabla Defensiva ===")
    print(df_def.to_string(index=False))
    print(f"\nInmunidades: {inm if inm else 'Ninguna'}")
    print(f"Resistencias: {res if res else 'Ninguna'}")
    print(f"Debilidades: {deb if deb else 'Ninguna'}")

    # Tabla ofensiva final
    mults_of, super_eff, neutral, poco, not_eff = tabla_ofensiva(individuo["tipo1"], individuo["tipo2"])
    df_of = pd.DataFrame([{"Defensor":d, "Multiplicador":m} for d,m in mults_of.items()]).sort_values("Multiplicador", ascending=False)
    print("\n=== Tabla Ofensiva ===")
    print(df_of.to_string(index=False))

    # Graficas
    plt.figure(figsize=(14,6))
    plt.subplot(1,2,1)
    plt.plot(fitness_hist_total, marker='o')
    plt.title(f"Fitness total ({nombre})")
    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.grid(True)

    plt.subplot(1,2,2)
    atacantes = list(mults_def.keys())
    valores = [mults_def[a] for a in atacantes]
    colors = ['green' if v<1 else ('gray' if v==1 else 'red') for v in valores]
    plt.bar(atacantes, valores, color=colors)
    plt.xticks(rotation=90)
    plt.axhline(1.0, color='black', linestyle='--')
    plt.ylabel("Multiplicador")
    plt.title(f"Defensiva Final ({individuo['tipo1']}/{individuo['tipo2']})")
    plt.tight_layout()
    plt.show()

    # Gráfico ofensivo final
    plt.figure(figsize=(12,5))
    defenders = list(mults_of.keys())
    vals_of = [mults_of[d] for d in defenders]
    colors_of = ['green' if v>1 else ('gray' if v==1 else 'red' if v==0 else 'orange') for v in vals_of]
    plt.bar(defenders, vals_of, color=colors_of)
    plt.xticks(rotation=90)
    plt.axhline(1.0, color='black', linestyle='--')
    plt.ylabel("Multiplicador")
    plt.title(f"Ofensiva Final ({individuo['tipo1']}/{individuo['tipo2']})")
    plt.tight_layout()
    plt.savefig("ofensiva_final.png")
    plt.show()

if __name__ == "__main__":
    main()
