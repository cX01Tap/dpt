from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! its me phanuruj'

if __name__ == 'phanuruj':
    app.run(debug=True, port=80)
