from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configura tu API Key de Google Gemini
genai.configure(api_key="TU_API_KEY_AQUI")  # <-- Reemplaza por tu API Key

# Crea instancia del modelo
model = genai.GenerativeModel("gemini-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    try:
        response = model.generate_content(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
