def leer_dfa(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()

        num_casos = int(contenido[0].strip())
        casos = []
        indice = 1

        for _ in range(num_casos):
            n_estados = int(contenido[indice].strip())
            indice += 1

            alfabeto = contenido[indice].strip().split()
            indice += 1

            estados_finales = set(map(int, contenido[indice].strip().split())) if contenido[indice].strip() else set()
            indice += 1

            transiciones = {}
            for _ in range(n_estados):
                fila = list(map(int, contenido[indice].strip().split()))
                estado_actual = fila[0]
                transiciones[estado_actual] = {alfabeto[i]: fila[i + 1] for i in range(len(alfabeto))}
                indice += 1

            casos.append((n_estados, alfabeto, estados_finales, transiciones))

        return casos

    except FileNotFoundError:
        print("Error: No se encontró el archivo casosDePrueba.txt")
        return []
    except ValueError as e:
        print(f"Error en el formato del archivo: {e}")
        return []

def encontrar_pares_equivalentes(n_estados, estados_finales, transiciones):
    particiones = [
        {estado for estado in range(n_estados) if estado in estados_finales},
        {estado for estado in range(n_estados) if estado not in estados_finales}
    ]
    particiones = [p for p in particiones if p]

    refinando = True
    while refinando:
        refinando = False
        nuevas_particiones = []

        for grupo in particiones:
            divisiones = {}
            for estado in grupo:
                clave = tuple(
                    next((i for i, part in enumerate(particiones) if transiciones[estado][simbolo] in part), None)
                    for simbolo in transiciones[estado]
                )
                divisiones.setdefault(clave, set()).add(estado)

            nuevas_particiones.extend(divisiones.values())

        if len(nuevas_particiones) > len(particiones):
            refinando = True
        particiones = nuevas_particiones

    equivalentes = []
    for grupo in particiones:
        estados = sorted(grupo)
        for i in range(len(estados)):
            for j in range(i + 1, len(estados)):
                equivalentes.append((estados[i], estados[j]))

    return sorted(equivalentes)

def main():
    nombre_archivo = "casosDePrueba.txt"
    casos = leer_dfa(nombre_archivo)

    if not casos:
        return

    for i, (n_estados, alfabeto, estados_finales, transiciones) in enumerate(casos):
        equivalentes = encontrar_pares_equivalentes(n_estados, estados_finales, transiciones)
        print(" ".join(f"({par[0]}, {par[1]})" for par in equivalentes))

if __name__ == "__main__":
    main()   








