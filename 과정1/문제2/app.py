from flask import Flask

app = Flask(__name__)

@app.route("/")
breakpoint()
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)