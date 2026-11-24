from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/voltear", methods=["POST"])
def voltear():
    datos = request.get_json()
    palabra = datos.get("palabra", "")
    palabra_volteada = palabra[::-1]
    print(f"Recibí '{palabra}' -> Devuelvo '{palabra_volteada}'")
    return jsonify({"volteada": palabra_volteada})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)