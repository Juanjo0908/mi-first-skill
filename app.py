from flask import Flask, jsonify

# ESTA ES LA LÍNEA CLAVE: El servidor busca esta variable 'app'
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "message": "¡Skill desplegada con éxito!",
        "version": "1.0.0"
    })

# Asegúrate de que tus funciones de ML estén después de la definición de 'app'
@app.route('/analyze', methods=['POST'])
def analyze():
    return jsonify({"result": "Analizador listo"})

# No es obligatorio para el servidor, pero ayuda en local
if __name__ == "__main__":
    app.run()
