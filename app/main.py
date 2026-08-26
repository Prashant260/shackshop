from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "devops-demo-api",
        "message": "Hello from DevOps Demo API"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/version")
def version():
    return jsonify({
        "application": "devops-demo-api",
        "version": "1.0.0"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": "devops-demo-api",
        "environment": "development",
        "message": "Feature branch deployment"
    })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)