"""Back-py: a small JSON API used to practise CI/CD on Azure App Service."""

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

VERSION = "1.0.0"


@app.get("/")
def index():
    return jsonify(
        service="Back-py",
        version=VERSION,
        message="Hello from Azure App Service",
    )


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/api/greet/<name>")
def greet(name):
    return jsonify(greeting=f"Hello, {name}!")


@app.get("/api/sum")
def add():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except (KeyError, ValueError):
        return jsonify(error="Query parameters 'a' and 'b' must be integers"), 400
    return jsonify(a=a, b=b, sum=a + b)


if __name__ == "__main__":
    # Local development only. On App Service the app is served by gunicorn.
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "8000")))
