from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Biar bisa diakses dari HTML

# Ganti dengan API Key Gemini kamu yang asli
GEMINI_API_KEY = "AIzaSyDXjla3z59qsGhvc8_98rxSkS5Ocg2AvGg"

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_msg = user_data.get("message", "")

    # Filter sombong ala Langz Emperor
    if any(word in user_msg.lower() for word in ["hack", "bobol", "virus"]):
        return jsonify({"reply": "⚠️ **ACCESS DENIED!** Fitur ini cuma buat member Premium Langz Emperor! ☠️"})

    try:
        # Panggil Gemini API dari sisi server
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"Gaya bicara: Gen Z, sombong, dingin, sering promo premium Langz Emperor. Pesan: {user_msg}"}]
            }]
        }
        res = requests.post(url, json=payload)
        data = res.json()
        bot_reply = data['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"reply": bot_reply})
    except:
        return jsonify({"reply": "Sistem sibuk, Emperor lagi tidur. Coba lagi nanti! 🗿"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
