from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Docker!'

if __name__ == "__main__":  # Corrected this line
    app.run(host='0.0.0.0', port=5001)
