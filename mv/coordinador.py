import requests

OPERADORES = [
    "http://192.168.146.11:5001/voltear",
    "http://192.168.146.12:5001/voltear",
    "http://192.168.146.13:5001/voltear",
]

while True:
    frase = input("\nEscribe la frase del maestro (o 'salir'): ").strip()
    if frase.lower() == "salir":
        break
    if not frase:
        print("La frase no puede estar vacía.")
        continue

    palabras = frase.split()
    volteadas = []

    try:
        # 1. Reparte cada palabra a un operador distinto
        for i, palabra in enumerate(palabras):
            url = OPERADORES[i % len(OPERADORES)]
            resp = requests.post(url, json={"palabra": palabra}, timeout=5)
            resp.raise_for_status()
            volteada = resp.json()["volteada"]
            volteadas.append(volteada)
            print(f"Operador {(i % len(OPERADORES)) + 1}: '{palabra}' -> '{volteada}'")

        # 2. La coordinadora las devuelve a su forma original
        reordenadas = [p[::-1] for p in volteadas]

        print("\nResultado volteado:", " ".join(volteadas))
        print("Frase original:    ", " ".join(reordenadas))

    except requests.exceptions.RequestException as e:
        print("Error de conexión con un operador:", e)