from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Servidor Flask funcionando correctamente en Vercel"

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        return f"✅ TikTok devolvió el código: {code}"
    else:
        return "❌ No se recibió ningún código desde TikTok"

@app.route('/terms')
def terms():
    return send_file("terms.html")

@app.route('/privacy')
def privacy():
    return send_file("privacy.html")

if __name__ == "__main__":
    app.run()
