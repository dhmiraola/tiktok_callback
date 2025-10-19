from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return "✅ Servidor Flask activo en Vercel (TikTok Callback listo)"

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        return f"✅ TikTok devolvió el código: {code}"
    else:
        return "❌ No se recibió ningún código desde TikTok"

@app.route('/terms')
def terms():
    return send_from_directory(BASE_DIR, 'terms.html')

@app.route('/privacy')
def privacy():
    return send_from_directory(BASE_DIR, 'privacy.html')

if __name__ == '__main__':
    app.run()
