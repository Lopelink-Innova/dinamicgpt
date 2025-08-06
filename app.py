from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from ia_config import IA_INSTRUCCIONES

app = Flask(__name__)
genai.configure(api_key="TU_API_KEY_AQUI")  # Reemplaza con tu clave

modelo = genai.GenerativeModel("gemini-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensajes = IA_INSTRUCCIONES + data["messages"]
    try:
        respuesta = modelo.generate_content(mensajes)
        return jsonify({'response': respuesta.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
