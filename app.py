from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generar_chiste(tema):
    # Pequeño "motor" de IA basado en plantillas
    plantillas = [
        f"¿Sabes por qué {tema} nunca falla? Porque siempre tiene una solución… aunque sea chapuza 😂",
        f"Dicen que {tema} es fácil… ¡hasta que lo intentas por primera vez!",
        f"Estaba pensando en {tema}, pero terminé pensando en una siesta. Mejor decisión 😅",
        f"¿Qué le dijo un {tema} a otro {tema}? ¡Nada, porque los {tema}s no hablan! 🤣",
        f"Quise impresionar hablando de {tema}, pero al final solo impresioné… a mi gato.",
        f"Mi amigo me dijo que {tema} era su pasión; yo le dije que mi pasión era procrastinar sobre {tema}.",
        f"Si {tema} fuera deporte, yo ya estaría lesionado desde el calentamiento.",
        f"Intenté aprender {tema} con un tutorial… ahora necesito un tutorial para entender el tutorial."
    ]
    return random.choice(plantillas)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chiste", methods=["POST"])
def api_chiste():
    data = request.get_json(silent=True) or {}
    tema = (data.get("tema") or "").strip()

    if not tema:
        tema = "programación"  # valor por defecto

    chiste = generar_chiste(tema)
    return jsonify({"chiste": chiste})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
