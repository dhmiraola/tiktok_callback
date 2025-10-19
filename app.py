from flask import Flask, request
app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"✅ TikTok devolvió el código: {code}", 200

if __name__ == "__main__":
    app.run()
